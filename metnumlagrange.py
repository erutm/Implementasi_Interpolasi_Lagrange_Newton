import numpy as np
import matplotlib.pyplot as plt

#Data (x: tegangan, y: waktu patah)
x_points = np.array([5, 12, 15, 22, 28, 33, 38, 45])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

#Fungsi untuk interpolasi metode polinom Lagrange
def lagrange_interpolation(x, x_points, y_points):
    def L(k, x):
        result = 1
        for i in range(len(x_points)):
            if i != k:
                result *= (x - x_points[i]) / (x_points[k] - x_points[i])
        return result
    
    result = 0
    for k in range(len(x_points)):
        result += y_points[k] * L(k, x)
    return result

#Fungsi pengujian interpolasi metode polinom Lagrange
def test_lagrange_interpolation():
    x_test = np.linspace(5, 40, 400)
    y_test = [lagrange_interpolation(x, x_points, y_points) for x in x_test]
    
    #Plot grafik hasil interpolasi Lagrange
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_points, 'o', label='Data Points')
    plt.plot(x_test, y_test, label='Lagrange Interpolation')
    plt.xlabel('Tegangan (kg/mm²)')
    plt.ylabel('Waktu Patah (jam)')
    plt.title('Interpolasi Metode Polinom Lagrange')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return x_test, y_test

#Memilih beberapa nilai x untuk melihat hasil interpolasi
x_values_to_test = [6, 13, 18, 24, 29, 32, 37, 39]
for x in x_values_to_test:
    y_interp = lagrange_interpolation(x, x_points, y_points)
    print(f'Interpolasi di x = {x} adalah y = {y_interp:.4f}')

#Memanggil fungsi untuk menguji dan memplot hasil interpolasi
x_test, y_test = test_lagrange_interpolation()