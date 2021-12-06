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

func part1 (data string) {
  dataSlice := strings.Split(strings.ReplaceAll(data, "\r\n", "\n"), "\n")

  count := 0
  dataLen := len(dataSlice)

  head := 0
  next := head + 1
  tail := dataLen - 1
  tailPrev := dataLen - 1

  for head <= tail {
    if dataSlice[head] < dataSlice[next] {
      count++
    }

    if dataSlice[tail] > dataSlice[tailPrev] {
      count++
    }

    head++
    next = head + 1
    tail--
    tailPrev = tail - 1
  }

  fmt.Println(count)
}

func part2 (data string) {
  dataSlice := strings.Split(strings.ReplaceAll(data, "\r\n", "\n"), "\n")

  count := 0
  dataLen := len(dataSlice)

  idx2 := 2
  idx1 := 1
  idx0 := 0
  prevSum := 0
  tailIdx2 := dataLen - 4
  tailIdx1 := dataLen - 3
  tailIdx0 := dataLen - 2
  prevTailSum := 0

  for idx2 < tailIdx0 {
    f, err := strconv.Atoi(dataSlice[idx2]); if err != nil { panic(err) }
    s, err := strconv.Atoi(dataSlice[idx1]); if err != nil { panic(err) }
    t, err := strconv.Atoi(dataSlice[idx0]); if err != nil { panic(err) }

    tf, err := strconv.Atoi(dataSlice[tailIdx2]); if err != nil { panic(err) }
    ts, err := strconv.Atoi(dataSlice[tailIdx1]); if err != nil { panic(err) }
    tt, err := strconv.Atoi(dataSlice[tailIdx0]); if err != nil { panic(err) }

    sum := f + s + t
    tailSum := tf + ts + tt

    if sum > prevSum {
      count++
    }

    if tailSum < prevTailSum {
      count++
    }

    idx0++
    idx1++
    idx2++
    tailIdx0--
    tailIdx2--
    tailIdx1--

    prevSum = sum
    prevTailSum = tailSum
  }

  fmt.Println(count)
}
