@main def task1: Unit = 
  var boardSize = 5
  val input = readInput
  val boards = input.tail.grouped(boardSize + 1).toList.map(list => list.tail)
  val splitBoards = boards.map(_.map(str => str.split(" ", 0).filter(_.nonEmpty).toList))
  val numbers = input(0).split(",").toList
  println(splitBoards.foreach{row => print(row); println})
  println(splitBoards(0).length)

def readInput =
  val source = scala.io.Source.fromFile("input.txt")
  val numbers = source.getLines.toList.map(line => line.toString)
  source.close()
  numbers