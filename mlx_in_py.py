import mlx.core as mx

sampling_rate2 = 1000
duration2 = 1
t2 = mx.linspace(0, duration2, int(sampling_rate2 * duration2))

freq12 = 5
freq22 = 50
#pi2 = mx.pi #there is no mx.pi AttributeError: module 'mlx.core' has no attribute 'pi'
pi2 = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
y12 = mx.sin(2 * pi2 * freq12 * t2)
y22 = mx.sin(2 * pi2 * freq22 * t2)
signal2 = y12 + y22

fft2 = mx.fft.fft(signal2)
fft2_abs = mx.abs(fft2)

print(fft2_abs)