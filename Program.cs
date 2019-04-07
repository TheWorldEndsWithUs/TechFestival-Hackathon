using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace Seperate
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> complaints = new List<string>();
            using (StreamReader sr = new StreamReader(@"C:\Users\adroi\Desktop\Complaints\Complaints Joined.txt"))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    complaints.Add(line);
                }
            }


            var folder = @"C:\Users\adroi\Desktop\Complaints\Complaint Files\";
            int counter = 0;
            foreach (string complaint in complaints)
            {
                using (StreamWriter sw = new StreamWriter(folder + "Complaint" + counter + ".txt"))
                {
                    sw.Write(complaint);
                }
                counter++;
            }
        }
    }
}
