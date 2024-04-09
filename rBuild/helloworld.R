# Load required libraries
library(ggplot2)

# Print "Hello, World!"
cat("Hello, World!\n")

# Define a vector of numbers
numbers <- c(1, 2, 3, 4, 5)

# Calculate the sum of numbers
total <- sum(numbers)

# Print the sum
cat("Sum of numbers:", total, "\n")

# Create a dataframe for plotting
df <- data.frame(numbers)

# Plot the numbers
ggplot(df, aes(x = numbers)) +
  geom_bar(fill = "blue", stat = "count") +
  labs(title = "Sum of Numbers", x = "Numbers", y = "Count") +
  theme_minimal()

# Save the plot to a file
ggsave("plot.png")

# Save the sum to a file
write(total, file = "sum.txt")
