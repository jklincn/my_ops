#include <torch/extension.h>

namespace my_ops {
at::Tensor ops1_cpu(at::Tensor a) { return a; }
PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {}

TORCH_LIBRARY(my_ops, m) { m.def("ops1(Tensor a) -> Tensor"); }

TORCH_LIBRARY_IMPL(my_ops, CPU, m) { m.impl("ops1", &ops1_cpu); }

} // namespace my_ops
