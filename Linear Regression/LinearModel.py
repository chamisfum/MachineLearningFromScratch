# linear regression from scratch

class LinearRegression():

    def __init__(self) -> None:
        """
            Inisiasi properti dalam contruct method untuk nilai intercept (b0) dan slope (b1)
        """
        self.b0 = None
        self.b1 = None
    
    def __sqrt(self, value):
        """
            Fungsi ini akan menghitung nilai akar kuadart dengan menggunakan rumus x^(1/2).
            

            return: Float of square root from input values
        """
        return (value ** (1/2))
    
    def __abs(self, value):
        """
            Fungsi ini menghitung nilai mutlak dengan menggunakan fungsi self.__sqrt() dari nilai parameter yang dikuadratkan.
            

            return: Float of absolute score from input values
        """
        return self.__sqrt((value**2))
    
    def __mean(self, values):
        """
            Fungsi ini menghitung hasil rata - rata dari nilai parameter value.
            Rumus rata - rata: total nilai parameter value / banyaknya nilai dari parameter value.
            

            return: Float of mean from input values
        """
        return sum(values) / float(len(values))

    def __mse(self, actual, predicted):
        """
            Fungsi untuk menghitung nilai kuadrat dari rata - rata error (galat) model. 
            Nilai galat dihitung dari nilai prediksi - nilai sesungguhnya (Ground truth) dari masing - masing data pengawasan.
            Selanjutnya nilai galat dijumlahkan dan dihitung nilai rata - rata galatnya.
            Hingga akhirnya fungsi ini akan mengembalikan nilai kuadrat dari rata - rata galatnya.
            

            return: Float of mse_score
        """
        sum_of_error = 0.0
        for i in range(len(actual)):
            prediction_error = predicted[i] - actual[i]
            sum_of_error += (prediction_error ** 2) 
        mse_score = sum_of_error / float(len(actual)) 
        return mse_score
    
    def __mae(self, actual, predicted):
        """
            Fungsi untuk menghitung nilai mutlak dari rata - rata error (galat) model. 
            Nilai galat dihitung dari nilai prediksi - nilai sesungguhnya (Ground truth) dari masing - masing data pengawasan.
            Selanjutnya nilai galat dijumlahkan dan dihitung nilai rata - rata galatnya.
            Hingga pada akhirnya fungsi ini mengembalikan nilai mutlak dari rata - rata nilai galat yang dihasilkan.
            

            return: Float of mae_score
        """
        sum_of_error = 0.0
        for i in range(len(actual)):
            prediction_error = predicted[i] - actual[i]
            sum_of_error += prediction_error    
        mae_score = self.__abs(sum_of_error / float(len(actual)))
        return mae_score

    def __rmse(self, actual, predicted):
        """
            Fungsi untuk menghitung nilai akar kuadrat dari rata - rata error (galat) kuadrat model. 
            Nilai galat dihitung menggunakan fungsi self.__mse() dari nilai actual dan predicted.
            Terakhir menghitung nilai akar kuadrat dari nilai yang dikembalikan oleh fungsi self.__mse() menggunakan fungsi self.__sqrt().
            
            

            return: Float of rmse_error
        """
        mean_error = self.__mse(actual, predicted)
        rmse_error = self.__sqrt(mean_error)
        return rmse_error
    
    def __r2(self, actual, predicted):
        """
            Fungsi untuk menghitung nilai R^2.
            Nilai R^2 didapatkan dari rumus: 1 - (total kuadrat galat / total kuadrat galat residual)
            

            return: Float of r2_score
        """
        first_error = 0
        second_error = 0
        for i in range(len(actual)):
            first_error += (actual[i] - self.__mean(actual)) ** 2
            second_error += (actual[i] - predicted[i]) ** 2
        r2_score = 1 - (second_error/first_error)
        return r2_score

    def __covariance(self, x, x_mean, y, y_mean):
        """
            Fungsi untuk menghitung kovarian (ukuran bagaimana perubahan dalam satu variabel dikaitkan dengan perubahan dalam variabel kedua) 
            dari variabel independen (x) dan variabel dependen (y).
            Nilai kovarian didapatkan dari rumus: \Sigma (x_{i}-x_{{\text{avg}}})(y_{i}-y_{{\text{avg}}})/(n-1). 
            

            return: Float of covariance
        """
        covariance = 0.0
        for i in range(len(x)):
            covariance += (x[i] - x_mean) * (y[i] - y_mean)
        return covariance

    def __variance(self, x, x_mean):
        """
            Fungsi untuk menghitung varian dari data x.
            Nilai varian didapatkan dari rumus: \Sigma [({\displaystyle x_{i}}x_{i} - x̅){\displaystyle ^{2}}^{2}]/(n - 1).
            

            return: Float of variance
        """
        return sum([(x - x_mean) ** 2 for x in x])
    
    def evaluate(self, actual, predicted, matric: str = 'mae'):
        """
            Fungsi ini digunakan untuk melakukan evaluasi model dengan menggunakan matriks evaluasi yang sudah di definisikan.
            Parameter matric disini menerima input nilai berupa string dengan mode yang bisa di pilih oleh user.
            Mode yang disediakan antara lain sebagai berikut:
                {
                    'mae'  : untuk mendapatkan nilai evaluasi model berupa mean absolute error
                    'mse'  : untuk mendapatkan nilai evaluasi model berupa mean square error
                    'rmse' : untuk mendapatkan nilai evaluasi model berupa root mean square error
                    'r2'   : untuk mendapatkan nilai evaluasi model berupa r^2 error
                    'all'  : untuk mendapatkan nilai evaluasi seluruh matric evaluasi baik itu ('mae', 'mse', 'rmse' ataupun 'r2').
                }
            User hanya diperkenankan memilih salah satu mode evaluasi yang disediakan, dan apabila user memasukkan mode evaluasi yang tidak
            terdaftar maka program akan menampikan pesan ValueError.
            Parameter actual digunakan untuk mendapatkan nilai ground truth dari data yang dievaluasi.
            Parameter predicted digunakan untuk mendapatkan nilai prediksi dari data yang dievaluasi.

            Seluruh parameter fungsi wajib ditentukan nilainya kecuali nilai parameter matric karena memiliki nilai default yaitu 'mae'

            return: evaluation score (float)
        """

        matric_mode = ['mae', 'mse', 'rmse', 'r2', 'all']
        if matric not in matric_mode:
            raise ValueError("Invalid matric evaluation mode. Expected matric mode: %s" % matric_mode)
        else:
            if matric == 'mae':
                return self.__mae(actual, predicted)
            elif matric == 'mse':
                return self.__mse(actual, predicted)
            elif matric == 'rmse':
                return self.__rmse(actual, predicted)
            elif matric == 'r2':
                return self.__r2(actual, predicted)
            else:
                evaluation_dict = {'mae'  : self.__mae(actual, predicted)[0],
                                   'mse'  : self.__mse(actual, predicted)[0],
                                   'rmse' : self.__rmse(actual, predicted)[0],
                                   'r2'   : self.__r2(actual, predicted)[0],
                                  }
                return evaluation_dict
   
    def fit(self, x, y):
        """
            Fungsi untuk melatih model dengan input parameter dependen (x) dan independen (y).

            return: list of intercept (b0) and slope (b1) value
        """
        x_mean, y_mean = self.__mean(x), self.__mean(y)
        self.b1 = self.__covariance(x, x_mean, y, y_mean) / self.__variance(x, x_mean)
        self.b0 = y_mean - self.b1 * x_mean
        return [self.b0[0], self.b1[0]]

    def predict(self, test):
        """
            Fungsi untuk melakukan prediksi data dengan rumus persamaan y_pred = aX + b

            return: list of prediction value (float)
        """
        predictions = list()
        for row in test:
            y_pred = self.b0 + self.b1 * row[0]
            predictions.append(y_pred[0])
        return predictions