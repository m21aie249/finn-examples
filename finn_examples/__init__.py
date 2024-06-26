# Copyright (c) 2022 Xilinx, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of Xilinx nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# workaround after finn-base is deprecated:
# the PYNQ drivers generated by the FINN compiler depend on a few submodules
# from FINN and QONNX, but we don't want to install the whole package on
# embedded platforms, so we bundle the necessary source files with finn_examples
# instead. but those source files appear under the finn_examples package,
# so we put them into sys.modules here.
# TODO this is a hacky solution at best - consider creating something like a
# finn-runtime package or remove these dependencies somehow.

import sys

import finn_examples.qonnx as qonnx

sys.modules["qonnx"] = qonnx

import finn_examples.qonnx.core.datatype as datatype  # noqa: E402

sys.modules["qonnx.core.datatype"] = datatype

import finn_examples.qonnx.util.basic as basic  # noqa: E402

sys.modules["qonnx.util.basic"] = basic

import finn_examples.finn.util.data_packing as data_packing  # noqa: E402

sys.modules["finn.util.data_packing"] = data_packing
