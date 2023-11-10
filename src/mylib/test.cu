#include <torch/extension.h>
#include <cooperative_groups.h>
#include <cuda/atomic>
// #include <iostream>

int myfunc(torch::Tensor z)
{
    z += 1;
    return 2;
    std::cout << "hello" << std::endl;
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m)
{
    m.def("myfunc", &myfunc, "myfunc");
}