#include <torch/extension.h>
#include <c10/cuda/CUDAGuard.h>

// cu 会交给 nvcc 编译
// cpp 会交给 gcc 编译

static __global__ void swish_forward(float* x, float* y, int n){
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if(i >= n) return;
    // swish
    y[i] = x[i] * (1 + exp(-x[i]));
}

at::Tensor forward(const at::Tensor x){
    // 设置当前的 device id
    const at::cuda::OptionalCUDAGuard device_guard(device_of(x));
    cudaStream_t stream = at::cuda::getCurrentCUDAStream();
    // auto options = torch::TensorOptions().dtype(x.dtype()).device(x.device());
    at::Tensor y = torch::zeros_like(x);

    dim3 block(512);
    dim3 grid((x.numel() + block.x - 1) / block.x);
    swish_forward<<<grid, block, 0, stream>>>(
        x.data_ptr<float>(), y.data_ptr<float>(), x.numel()
    );

    printf("x.shape = %d x %d\n", x.size(0), x.size(1));
    return y;
}


PYBIND11_MODULE(TORCH_EXTENSION_NAME, m){
    m.def("forward", &forward); // 定义函数名
}

