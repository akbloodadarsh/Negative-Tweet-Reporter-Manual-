from sklearn import naive_bayes


def MultinomialNBAlgo(x_train_vft, y_train, x_test_vft, y_test, vec):
    # print("Multinomial Naive Bayes")
    mnb = naive_bayes.MultinomialNB()
    mnb.fit(x_train_vft, y_train)
    y_predict_class = mnb.predict(x_test_vft)
    if mnb.predict(vec) == [1]:
        return 'Positive'
    else:
        return 'Negative'
