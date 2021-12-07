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

  counter := [12]int{}

  for _, s := range(dataSlice) {
    chars := strings.Split(s, "")

    for i, bit := range(chars) {
      if bit == "1" {
        counter[i]++
      }
    }
  }

  var gamma, epsilon string
  for _, count := range(counter) {
    if count > len(dataSlice) / 2 {
      gamma = gamma + "1"
      epsilon = epsilon + "0"
    } else {
      gamma = gamma + "0"
      epsilon = epsilon + "1"
    }
  }

  gammaInt, err := strconv.ParseInt(gamma, 2, 64); if err != nil {
    panic(err)
  }

  epsilonInt, err := strconv.ParseInt(epsilon, 2, 64); if err != nil {
    panic(err)
  }

  fmt.Println(gammaInt * epsilonInt)
}

func part2(data string) {
  dataSlice := strings.Split(strings.ReplaceAll(data, "\r\n", "\n"), "\n")

  oxygenGeneratorRating, err := strconv.ParseInt(recurse(dataSlice, 0, true)[0], 2, 64); if err != nil {
    panic(err)
  }
  co2ScrubberRating, err := strconv.ParseInt(recurse(dataSlice, 0, false)[0], 2, 64); if err != nil {
    panic(err)
  }

  fmt.Println(oxygenGeneratorRating * co2ScrubberRating)
}

func recurse(dataSlice []string, idx int, oxygen bool) []string {
  if len(dataSlice) == 1 {
    return dataSlice
  } else {
   var zeroes, ones int
    filteredSlice := []string{}
    spot := "0"

    for _, s := range(dataSlice) {
      if s == "" {
        continue
      }
      chars := strings.Split(s, "")

      if chars[idx] == "0" {
        zeroes++
      } else {
        ones++
      }
    }

    if (oxygen && ones >= zeroes) || (!oxygen && zeroes > ones) {
      spot = "1"
    }

    for _, s := range(dataSlice) {
      if s == "" {
        continue
      }
      chars := strings.Split(s, "")

      if chars[idx] == spot {
        filteredSlice = append(filteredSlice, s)
      }
    }

    idx++
    return recurse(filteredSlice, idx, oxygen)
  }
}
