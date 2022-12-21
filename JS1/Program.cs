Console.Clear();



string[] Array = new string[5];

Console.WriteLine("Заполните массив: ");
for (int i = 0; i < 5; i++)
{
    Array[i] = Console.ReadLine();

}

Console.WriteLine();
Console.Write("[" + string.Join(",", Array) + "]");
Console.Write(" -> [ ");

for (int i = 0; i < 5; i++)
{

    if (Array[i].Length <= 3)
    {
        Console.Write($"{Array[i]},");
    }
}
Console.Write("\b]");