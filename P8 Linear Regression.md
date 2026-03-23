**P8: Linear Regression**



x = c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)

y = c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

relation = lm(y\~x)

print(relation)



print(summary(relation))



a = data.frame(x = 170)

result = predict(relation, a)

print(result)



png(file="linearregression.png")

plot(y, x, col = "blue", main = "Height \& Weight Regression", abline(lm(x \~ y)), cex = 1.3, pch = 16, xlab = "Weight in kg", ylab = "Height in cm")

dev.off()





**What is Linear Regression?**

Linear Regression is a supervised learning algorithm used to model the relationship between a dependent variable (Y) and an independent variable (X).

It predicts continuous values by fitting a straight line (regression line) through the data.



**Step 1: Dataset Creation**

* x = c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
* y = c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

x → Height (independent variable).

y → Weight (dependent variable).



**Step 2: Build Regression Model**

* relation = lm(y \~ x)
* print(relation)
* print(summary(relation))

lm() → Linear Model function.

Fits regression line: 𝑦 = 𝑎 + 𝑏 ⋅ 𝑥

summary() → shows coefficients, R² value, and significance.



**Step 3: Prediction**

* a = data.frame(x = 170)
* result = predict(relation, a)
* print(result)

Predicts weight for a person with height = 170 cm.



**Step 4: Visualization**

* png(file="linearregression.png")
* plot(y, x, col = "blue", main = "Height \& Weight Regression", abline(lm(x \~ y)), cex = 1.3, pch = 16, xlab = "Weight in kg", ylab = "Height in cm")
* dev.off()

used to open a graphics device that will save the next plot you create into a PNG image file called linearregression.png.

plot(y, x) → Creates a scatter plot of your dataset (Weight vs Height).

col = "blue" → Makes the points blue.

main → Sets the title of the plot.

abline(lm(x \~ y)) → Adds the regression line to the plot.

cex = 1.3 → Increases the size of the points.

pch = 16 → Uses solid circle markers for points.

xlab / ylab → Labels the axes.

dev.off() is the “save and close” step for your plot image.



**Summary**

Linear Regression is used to predict continuous outcomes.

This practical demonstrates:

* Creating dataset (Height vs Weight).
* Building regression model.
* Predicting new values.
* Visualizing regression line.

