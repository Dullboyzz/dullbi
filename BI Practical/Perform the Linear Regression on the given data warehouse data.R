# Define height (x) and weight (y) data
x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)
relation <- lm(x ~ y)  
png(file = "linearregression.png")
plot(y, x, col = "blue", main = "Height & Weight Regression", 
     cex = 1.3, pch = 16, xlab = "Weight in kg", ylab = "Height in cm")
abline(relation, col = "red", lwd = 2)
dev.off()
