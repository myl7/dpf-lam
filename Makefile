format:
	find dpf_base dpf_gpu dpf_wrapper.cu \( -name '*.h' -o -name '*.c' -o -name '*.cpp' -o -name '*.cc' -o -name '*.cu' \) -exec clang-format -i {} +
