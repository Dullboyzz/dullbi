newiris <- iris
newiris$Species <- NULL
kc <- kmeans(newiris, 3)
print(kc)
table(iris$Species, kc$cluster)
png(file = "kmeans_clusters.png")
plot(newiris$Sepal.Length, newiris$Sepal.Width, 
     col = kc$cluster, pch = 16, cex = 1.5, 
     xlab = "Sepal Length", ylab = "Sepal Width", 
     main = "K-Means Clustering of Iris Data")
points(kc$centers[, c("Sepal.Length", "Sepal.Width")], 
       col = 1:3, pch = 8, cex = 3, lwd = 2)
dev.off()
