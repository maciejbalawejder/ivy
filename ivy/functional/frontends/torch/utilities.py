import ivy
from ivy.functional.frontends.torch.func_wrapper import to_ivy_arrays_and_back


@to_ivy_arrays_and_back
def result_type(tensor, other):
    return ivy.result_type(tensor, other)


@to_ivy_arrays_and_back
def _assert(condition, message):
    return ivy._assert(condition, message)
