package main

import (
  "fmt"
  "os"
  "strings"
  "strconv"
)

func main () {
  data, err := os.ReadFile("input.txt")
  if err != nil {
    panic(err)
  }

  strData := string(data)

  part1(strData)
  part2(strData)
}

func part1(data string) {
  dataSlice := strings.Split(strings.ReplaceAll(data, "\r\n", "\n"), "\n")

  var x, y int

  for _, command := range(dataSlice) {
    if command == "" {
      continue
    }
    commandSlice := strings.Split(command, " ")
    movement, err := strconv.Atoi(commandSlice[1]); if err != nil {
      panic(err)
    }

    switch commandSlice[0] {
      case "forward":
        x = x + movement
      case "up":
        y = y - movement
      case "down":
        y = y + movement
    }
  }

  fmt.Println(x * y)
}

func part2(data string) {
  dataSlice := strings.Split(strings.ReplaceAll(data, "\r\n", "\n"), "\n")

  var x, y, aim int

  for _, command := range(dataSlice) {
    if command == "" {
      continue
    }
    commandSlice := strings.Split(command, " ")
    value, err := strconv.Atoi(commandSlice[1]); if err != nil {
      panic(err)
    }

    if commandSlice[0] == "down" {
      aim = aim + value
    } else if commandSlice[0] == "up" {
      aim = aim - value
    } else if commandSlice[0] == "forward" {
      x = x + value
      y = y + aim * value
    }
  }

  fmt.Println(x * y)
}
