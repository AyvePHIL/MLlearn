import matplotlib.pyplot as plt


def estimator(x, y):
    mean_x = sum(x) / len(x)
    mean_y = sum(y) / len(y)

    # Initiate a for loop for calculating the slope and y-intercept
    r_num = []
    r_den_one = []
    r_den_two = []
    if len(x) == len(y):
        for i in range(len(x)):
            r_num.append(((x[i] - mean_x) * (y[i] - mean_y)))
            r_den_one.append((x[i] - mean_x) ** 2)
            r_den_two.append((y[i] - mean_y) ** 2)
    else:
        print('The Input Data does not have squared dimensions, see you data source!')

    # Initiate the Sum of squares terms
    SS_xy = sum(r_num)
    SS_xx = sum(r_den_one)
    SS_yy = sum(r_den_two)

    # Compute Terms needed!
    r = SS_xy / ((SS_xx * SS_yy) ** 0.5)  # Pearson's coefficient

    sd_y = (SS_yy / (len(y) - 1)) ** 0.5  # Standard deviation of data points from y
    sd_x = (SS_xx / (len(x) - 1)) ** 0.5  # Standard deviation of data points from y

    slope = r * (sd_y / sd_x)  # Slope of linear approximation line (>0 means y is directly proportional to x)
    y_intercept = mean_y - slope * mean_x  # y-intercept when x (our independent variable) is zero!

    SSE = SS_yy - slope * SS_xy  # Sum of Square ERROR (SSE)
    variance_error = SSE / (
                len(x) - 2)  # Variance error (the smaller the better) in relation to our linear relationship
    sd_error = (variance_error) ** 0.5  # Standard error, the smaller the better!

    # Begin plotting a scatter of the data and label as required
    plt.scatter(x, y)
    plt.xlabel("length [mm]")
    plt.ylabel("temperature [deg Celcius]")
    plt.title("Metal Rod Length Measured at Varying Temperatures")
    # plt.show()

    print('Therefore, y = ' + str(slope) + 'x + ' + str(y_intercept), 'With a Standard Deviation Error of : ' + str(sd_error), sep = "\n")

x = [43, 21, 25, 42, 57, 59]
y = [99, 65, 79, 75, 87, 81]
estimator(x, y)
