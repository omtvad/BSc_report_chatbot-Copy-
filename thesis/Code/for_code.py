# generate parameter ranges
kernels = np.array(['rbf', 'sigmoid', 'poly'])
nus = np.array([0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.000000000001])
gammas = np.logspace(-8, 4, 21) # 21 values from logarithmic range 10e-8 to 10e4

# iterate through parameter combinations
for param_kernel in kernels:
    for param_nu in nus:
        for param_gamma in gammas:

	    # initialize one-class SVM with current combination and train model
            clf = OneClassSVM(nu=param_nu, kernel=str(param_kernel), gamma=param_gamma)
            clf.fit(train_set)
            
	    # predict/ validate model on test set
            y_pred_test = clf.predict(test_set)

	    # calculate precision
            precision = metrics.precision_score(y_true, y_pred, pos_label=-1, average='binary')

            if precision > (0.5):
                # Save current parameters, precision and visualization