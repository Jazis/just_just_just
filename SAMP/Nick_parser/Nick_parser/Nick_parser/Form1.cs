using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using SampAPI;
using System.Threading;
using System.IO;

namespace Nick_parser
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private async void parse()
        {
            for (uint i = 0; i < 1000; i++)
            {
                try
                {
                    textBox1.Text = textBox1.Text + SampAPI.RemotePlayer.GetPlayerNameById(i) + "\n";
                    Thread.Sleep(100);
                }
                catch
                {

                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            parse();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SaveFileDialog savefile = new SaveFileDialog();
            savefile.Title = "Save nicks";
            savefile.Filter = "txt files(*.txt)| *.txt";
            savefile.RestoreDirectory = true;
            if (savefile.ShowDialog() == DialogResult.OK)
            {
                File.WriteAllText(savefile.FileName, textBox1.Text);
            }
        }
    }
}

