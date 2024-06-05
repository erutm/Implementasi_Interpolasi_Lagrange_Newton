import numpy as np
import matplotlib.pyplot as plt

#Data (x: tegangan, y: waktu patah)
x_points = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y_points = np.array([40, 30, 25, 40, 18, 20, 22, 15])

#Fungsi untuk interpolasi metode polinomial Newton
def newton_interpolation(x, x_points, y_points):
    n = len(x_points)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y_points

    for j in range(1, n):
        for i in range(n-j):
            divided_diff[i, j] = (divided_diff[i+1, j-1] - divided_diff[i, j-1]) / (x_points[i+j] - x_points[i])

    def newton_poly(x):
        result = divided_diff[0, 0]
        term = 1.0
        for i in range(1, n):
            term *= (x - x_points[i-1])
            result += divided_diff[0, i] * term
        return result

    return newton_poly(x)

#Fungsi pengujian interpolasi Newton
def test_newton_interpolation():
    x_test = np.linspace(5, 40, 400)
    y_test = [newton_interpolation(x, x_points, y_points) for x in x_test]
    
    #Plot hasil interpolasi metode polinom Newton
    plt.figure(figsize=(10, 6))
    plt.plot(x_points, y_points, 'o', label='Data Points')
    plt.plot(x_test, y_test, label='Newton Interpolation')
    plt.xlabel('Tegangan (kg/mm²)')
    plt.ylabel('Waktu Patah (jam)')
    plt.title('Interpolasi Metode Polinom Newton')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return x_test, y_test

#Memilih beberapa nilai x untuk melihat hasil interpolasi
x_values_to_test = [6, 13, 18, 24, 29, 32, 37, 39]
for x in x_values_to_test:
    y_interp = newton_interpolation(x, x_points, y_points)
    print(f'Interpolasi di x = {x} adalah y = {y_interp:.4f}')

#Memanggil fungsi untuk menguji dan memplot hasil interpolasi
x_test, y_test = test_newton_interpolation()