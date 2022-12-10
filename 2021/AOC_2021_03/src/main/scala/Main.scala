import scala.compiletime.ops.int
import scala.collection.mutable.ListBuffer
import java.util.Collection
@main def task1: Unit = 
  val input = readInput
  val inputSplit = input.map(str => str.sliding(1).toList)
  val transposed = inputSplit.transpose.toList
  val avg = (transposed.map(list => list.map(str => str.toDouble))).map(list => (average(list)).round.toInt)
  val gamma = Integer.parseInt(avg.mkString, 2)
  val epsilon = Integer.parseInt(avg.map{nb => nb match {case 0 => 1 case 1 => 0} }.mkString, 2)

  println(avg.mkString)
  println(avg.map{nb => nb match {case 0 => 1 case 1 => 0} }.mkString)
  println(gamma * epsilon)


@main def task2: Unit =
  val input = ListBuffer.empty ++= readInput
  var count = 0
  while input.length > 1 do
    val temp = ListBuffer.empty[Double]
    input.foreach{ word => temp += word.charAt(count).toString.toDouble}
    val wordsToBeRemoved = ListBuffer.empty[String]
    if (average(temp.toList) >= 0.5) then
      input.foreach{word => if word.charAt(count) == '0' then wordsToBeRemoved += word}
    else
      input.foreach{word => if word.charAt(count) == '1' then wordsToBeRemoved += word}

    wordsToBeRemoved.foreach{word => input -= word}
    count += 1

  val oxygen = Integer.parseInt(input(0).mkString, 2)  

  val input2 = ListBuffer.empty ++= readInput
  count = 0
  while input2.length > 1 do
    val temp = ListBuffer.empty[Double]
    input2.foreach{ word => temp += word.charAt(count).toString.toDouble}
    val wordsToBeRemoved = ListBuffer.empty[String]
    if (average(temp.toList) >= 0.5) then
      input2.foreach{word => if word.charAt(count) == '1' then wordsToBeRemoved += word}
    else
      input2.foreach{word => if word.charAt(count) == '0' then wordsToBeRemoved += word}

    wordsToBeRemoved.foreach{word => input2 -= word}
    count += 1

  val carbondioxide = Integer.parseInt(input2(0).mkString, 2)  

  print(oxygen * carbondioxide)

 

def readInput =
  val source = scala.io.Source.fromFile("input.txt")
  val numbers = source.getLines.toList.map(line => line.toString)
  source.close()
  numbers

def average(list: List[Double]): Double =
  list.sum / list.length 