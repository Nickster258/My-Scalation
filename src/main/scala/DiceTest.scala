import scalation.mathstat._
import scalation.random.Randi

object DiceTest extends App:

    val dice = Randi (1, 6)
    val x    = VectorD.range (0, 13)
    val freq = new VectorD (13)
    for i <- 0 until 10000 do
        val sum = dice.igen + dice.igen
        freq(sum) += 1
    end for
    new Plot (x, freq)

end DiceTest 

