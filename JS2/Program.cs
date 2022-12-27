class Program
{
    public static void Main(string[] args)
    {
        int[] array = { 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 };
        int[] res = QuickSort(array, 0, array.Length - 1);
        Console.Write("Your Array = {" + string.Join(", ", res) + "}");

        int[] QuickSort(int[] arr, int minIndex, int maxIndex)
        {
            if (minIndex >= maxIndex) return arr;
            int pivot = GetPivotIndex(arr, minIndex, maxIndex);
            QuickSort(arr, minIndex, pivot - 1);
            QuickSort(arr, pivot + 1, maxIndex);
            return arr;
        }
        int GetPivotIndex(int[] ar, int minIn, int maxIn)
        {
            int pivotIndex = minIn - 1;
            for (int i = minIn; i <= maxIn - 1; i++)
            {
                if (ar[i] < ar[maxIn])
                {
                    pivotIndex++;
                    Swap(ar, i, pivotIndex);
                }
            }
            pivotIndex++;
            Swap(ar, pivotIndex, maxIn);
            return pivotIndex;
        }
        void Swap(int[] inputArray, int leftValue, int rightValue)
        {
            int temp = inputArray[leftValue];
            inputArray[leftValue] = inputArray[rightValue];
            inputArray[rightValue] = temp;
        }
    }
}