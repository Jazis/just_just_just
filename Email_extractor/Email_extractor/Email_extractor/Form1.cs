using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Windows.Forms.VisualStyles;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.IO;

namespace Email_extractor
{
    public partial class Form1 : Form
    {
        IWebDriver driver = new ChromeDriver();
        public Form1()
        {
            InitializeComponent();

        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {



        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Auction_Start();
        }

        private void Auction_Start()
        {
            Task.Run(async () =>
            {
                while (1 > 0)
                {
                    Thread.Sleep(1000);
                    string url_s = driver.Url.ToString();
                    if (listBox1.Items.Contains(url_s))
                    {

                    }
                    else
                    {
                        if (driver.Url == "data:.")
                        {

                        }
                        var list0 = new List<string>();
                        listBox1.Items.Add(driver.Url.ToString());
                        label1.Text = listBox1.Items.Count.ToString();

                        string page_source = driver.PageSource;
                        int counter = page_source.Split(' ').Count();
                        for (int i = 0; i < counter; i++)
                        {
                            string mailto = "mailto:";
                            if (page_source.Split(' ')[i].Contains('@') && page_source.Split(' ')[i].Contains('.') && page_source.Split(' ')[i].Contains(mailto))
                            {
                                listBox2.Items.Add(page_source.Split(' ')[i].Split(':')[1].Split('"')[0].Replace("\n", ""));
                                label2.Text = listBox2.Items.Count.ToString();

                            }
                            if (page_source.Split(' ')[i].Contains('@') && page_source.Split(' ')[i].Contains('.'))
                            {
                                listBox2.Items.Add(page_source.Split(' ')[i]);
                                label2.Text = listBox2.Items.Count.ToString();

                            }
                        }
                    }
                }
            });
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var savedial = new SaveFileDialog();
            savedial.Filter = "Text (*.txt)|*.txt";
            if (savedial.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                using (var sw = new StreamWriter(savedial.FileName, false))
                    foreach (var item in listBox1.Items)
                        sw.Write(item.ToString() + Environment.NewLine);
                MessageBox.Show("Success");
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            var savedial = new SaveFileDialog();
            savedial.Filter = "Text (*.txt)|*.txt";
            if (savedial.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {
                using (var sw = new StreamWriter(savedial.FileName, false))
                    foreach (var item in listBox2.Items)
                        sw.Write(item.ToString() + Environment.NewLine);
                MessageBox.Show("Success");
            }
        }
    }
}
