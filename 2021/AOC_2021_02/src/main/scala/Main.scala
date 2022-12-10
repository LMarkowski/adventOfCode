

@main def task1: Unit = 
  val commands = readInput
  val commamdsSplit = commands.map(x => x.split(" ").toList)
  var x=0
  var y=0
  var aim=0
  commamdsSplit.foreach{ list =>
    list(0) match {
      case "forward" => 
        x += list(1).toInt
        y += aim * list(1).toInt
      case "up" => aim -= list(1).toInt
      case "down" => aim += list(1).toInt     
    }
  }
  
  print(x*y)


def readInput =
  val source = scala.io.Source.fromFile("input.txt")
  val numbers = source.getLines.toList.map(line => line.toString)
  source.close()
  numbers


