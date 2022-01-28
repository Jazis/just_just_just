using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            using (openFileDialog1 = new OpenFileDialog())
            {
                openFileDialog1.InitialDirectory = "c:\\";
                openFileDialog1.Filter = "txt files (*.txt)|*.txt|All files (*.*)|*.*";
                if (openFileDialog1.ShowDialog() == DialogResult.OK)
                {
                    label1.Text = openFileDialog1.FileName;
                }
            }
        }

        private async void button2_Click(object sender, EventArgs e)
        {
            try
            {
                Directory.CreateDirectory(Directory.GetCurrentDirectory() + "/sorted");
            }
            catch (IOException)
            {
                MessageBox.Show("Folder already exist");
            }
            int counter = 0;
            using (StreamReader st = new StreamReader(label1.Text, System.Text.Encoding.Default))
            {
                string line;
                while ((line = st.ReadLine()) != null)
                {
                    string qwer_bukv = Convert.ToString(line);
                    string mystr = "";
                    for (int i = 0; i < qwer_bukv.Length; i++)
                    {
                        if(char.IsLetter(qwer_bukv[i]) || char.IsDigit(qwer_bukv[i]) || char.IsSymbol(qwer_bukv[i]))
                            if (i > 1)
                                break;
                            else
                                mystr += qwer_bukv[i];
                    }
                    try
                    {
                        string two_bukv = mystr;
                        string path = Convert.ToString(Directory.GetCurrentDirectory()) + "/sorted/" + two_bukv.ToLower() + ".txt";
                        using (StreamWriter sw = new StreamWriter(path, true, System.Text.Encoding.Default))
                        {
                            await sw.WriteLineAsync(line);
                            counter += 1;
                        }
                    }
                    catch (Exception ex) { }
                }
            }
            MessageBox.Show("Base has been sorted - " + counter);
        }

        private async void button3_Click(object sender, EventArgs e)
        {
            try
            {
                Directory.CreateDirectory(Directory.GetCurrentDirectory() + "/domain_sorted");
            }
            catch (IOException)
            {
                MessageBox.Show("Folder already exist");
            }
            int counter = 0;
            using (StreamReader st = new StreamReader(label1.Text, System.Text.Encoding.Default))
            {
                string line;
                while ((line = st.ReadLine()) != null)
                {
                    if (line.Contains(".ru:"))
                    {
                        try
                        {
                            string path = Convert.ToString(Directory.GetCurrentDirectory()) + "/domain_sorted/ru_base.txt";
                            using (StreamWriter sw = new StreamWriter(path, true, System.Text.Encoding.Default))
                            {
                                await sw.WriteLineAsync(line);
                                counter += 1;
                            }
                        }
                        catch (Exception ex) { }
                    }
                    else
                    {
                        try
                        {
                            string path = Convert.ToString(Directory.GetCurrentDirectory()) + "/domain_sorted/other.txt";
                            using (StreamWriter sw = new StreamWriter(path, true, System.Text.Encoding.Default))
                            {
                                await sw.WriteLineAsync(line);
                                counter += 1;
                            }
                        }
                        catch (Exception ex) { }
                    }

                }
            }
            MessageBox.Show("Base has been sorted - " + counter);
        }
    }
}
