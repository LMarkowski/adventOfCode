import scala.compiletime.ops.int
@main def task1 : Unit =
  val numbers = readInput
  println(countIncreasions(numbers))

@main def task2 : Unit =
  val numbers = readInput
  val slides = numbers.sliding(3).toList.map(slide => slide.sum)
  println(countIncreasions(slides))


def countIncreasions(list:List[Int]) : Int =
  list.zip(list.tail).count((a, b) => a < b)

def readInput =
  val source = scala.io.Source.fromFile("input.txt")
  val numbers = source.getLines.toList.map(line => line.toInt)
  source.close()
  numbers



