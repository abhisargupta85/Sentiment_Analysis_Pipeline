# 1. Install necessary packages (only run this once if needed)
# install.packages("readr")
# install.packages("ggplot2")
# install.packages("dplyr")

# 2. Load the libraries
library(readr)
library(ggplot2)
library(dplyr)

# NOTE: Replace 'sentiment_results_YYYYMMDD.csv' with the actual filename created by the Python script
file_name <- "sentiment_results_20251005.csv" # Update the date here!

# 3. Load the data created by the Python script
sentiment_data <- read_csv(file_name)

# 4. Perform basic statistical aggregation
cat("--- Sentiment Summary Table ---\n")
sentiment_summary <- sentiment_data %>%
  group_by(sentiment) %>%
  summarise(
    Count = n(),
    Percentage = round(n() / nrow(.) * 100, 1),
    Average_Compound_Score = round(mean(compound), 4)
  )

print(sentiment_summary)

# 5. Create a visualization
sentiment_plot <- ggplot(sentiment_data, aes(x = sentiment, fill = sentiment)) +
  geom_bar(width = 0.7) +
  labs(
    title = paste("Customer Sentiment Distribution for Extracted Reviews"),
    subtitle = "Analysis performed using VADER (Python)",
    x = "Sentiment Category",
    y = "Number of Reviews"
  ) +
  # Custom theme for a clean look
  theme_minimal(base_size = 14) +
  scale_fill_manual(values = c("Negative" = "#E15759", "Neutral" = "#B0B0B0", "Positive" = "#59A14F")) +
  # Add labels for counts
  geom_text(stat='count', aes(label=..count..), vjust=-0.5, size=5) +
  # Remove the legend since the colors are already on the axis
  guides(fill = "none")

# Display the plot in the R environment
print(sentiment_plot)

# 6. Finally save the plot
ggsave("sentiment_distribution_report.png", plot = sentiment_plot, width = 9, height = 6)

cat("\n--- R Reporting Finished ---\n")

cat("Statistical summary printed. Visualization saved as 'sentiment_distribution_report.png'.\n")
