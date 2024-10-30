import random
import time
import dpf

random.seed(time.time())
dpf.test_cpu_dpf()
dpf.test_cpu_dpf_one_hot()
dpf.test_gpu_dpf()
dpf.test_gpu_dpf_nopad()
dpf.test_gpu_dpf_sweep()
dpf.test_gpu_dpf_perf()

# dpf.test_cpu_dpf_perf() # commented out because it is slow
