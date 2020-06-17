source("/home/stanley-yu/Documents/algorithms/bubblesort/bubblesort.R")
library(testthat)

context("bubble sort")

test_that("Sort pre-sorted array", {
  vec <-  c(5,10,15,20,25,30);
  expect_equal(bubbleSort(vec), c(5,10,15,20,25,30));
})

test_that("Sort reverse sorted array", {
  vec <- c(150,83,23,12,10,6.2,5);
  expect_equal(bubbleSort(vec), c(5,6.2,10,12,23,83,150));
})

test_that("Sort mixed array", {
  vec <- c(3,2,1,4,5);
  expect_equal(bubbleSort(vec), c(1,2,3,4,5));
})

message("All tests passed for exercise: bubble sort.")