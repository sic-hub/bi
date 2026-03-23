P10: Logistic Regression 



direct copy - paste:



hours <- c(1,2,3,4,5,6,7,8) 

result <- c(0,0,0,0,1,1,1,1) 

data <- data.frame(hours, result) 



model <- glm(result \~ hours, data=data, family=binomial) 

summary(model) 



predicted\_prob <- predict(model, type="response") 

predicted\_prob 



predicted\_class <- ifelse(predicted\_prob > 0.5, 1, 0) 

predicted\_class 



table(Predicted = predicted\_class, Actual = data$result)

plot(data$hours, data$result, xlab="Study Hours", ylab="Pass(1)/Fail(0)", main="Logistic Regression")

curve(predict(model, data.frame(hours=x), type="response"), add=TRUE, col="blue") 







**What is Logistic Regression?**

Logistic Regression is a supervised machine learning algorithm used for classification problems.

Instead of predicting continuous values (like linear regression), it predicts probabilities between 0 and 1.

Uses the sigmoid (logistic) function to convert inputs into probabilities.

Commonly applied in binary classification tasks (e.g., pass/fail, spam/not spam, disease/no disease).



**Step 1: Dataset Creation**

* hours <- c(1,2,3,4,5,6,7,8)
* result <- c(0,0,0,0,1,1,1,1)
* data <- data.frame(hours, result)

Creates a dataset with study hours (independent variable) and pass/fail result (dependent variable).

0 = Fail, 1 = Pass.



**Step 2: Logistic Regression Model**

* model <- glm(result \~ hours, data=data, family=binomial)
* summary(model)

Fits a logistic regression model.

glm() → Generalized Linear Model.

family=binomial → specifies logistic regression.

result \~ hours → predicts result based on study hours.

summary(model) → shows coefficients, significance, and model fit.



**Step 3: Predict Probabilities**

* predicted\_prob <- predict(model, type="response")

Predicts probability of passing for each student.

Output is between 0 and 1 (e.g., 0.2 means 20% chance of passing).



**Step 4: Convert Probabilities to Classes**

* predicted\_class <- ifelse(predicted\_prob > 0.5, 1, 0)

Converts probabilities into binary classes.

If probability > 0.5 → Pass (1).

Else → Fail (0).



**Step 5: Confusion Matrix**

* table(Predicted = predicted\_class, Actual = data$result)

Compares predicted results with actual results.

Shows True Positives, True Negatives, False Positives, False Negatives.



**Step 6: Graphical Representation**

* plot(data$hours, data$result, xlab="Study Hours", ylab="Pass(1)/Fail(0)", main="Logistic Regression")
* curve(predict(model, data.frame(hours=x), type="response"), add=TRUE, col="blue")

Plots data points (hours vs pass/fail).

Adds the S‑shaped logistic curve showing probability trend.



**Summary**

Logistic Regression is used to predict categorical outcomes (Pass/Fail).

The code builds a model, predicts probabilities, converts them into classes, evaluates with a confusion matrix, and visualizes with a logistic curve.

It demonstrates how study hours influence the probability of passing.





