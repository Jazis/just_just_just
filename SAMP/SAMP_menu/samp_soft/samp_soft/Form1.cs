using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Memory;
using System.Threading;
using SampAPI.Commands;
using SampAPI;
using System.Drawing.Design;
using System.IO;

namespace samp_soft
{
    public partial class Form1 : Form
    {
        List<string> list0 = new List<string>();
        public List<string> list1 = new List<string>();

        public Boolean _isWorking;
        Mem meme = new Mem();
        //public static string x_coord = "gta_sa.exe+0x0044CEB8,FDC";
        public static string nicks = "samp.dll+0x0012C7BC,1C";
        public static string x_coord = "samp.dll+0x00217678,30";
        public static string y_coord = "samp.dll+0x00217678,34";
        public static string z_coord = "samp.dll+0x00217678,38";
        public static string full_car_hp = "samp.dll+0x00186E04,4C0";
        //samp.dll+0x00186E04,4C0,B4,0,298,20,E0,8
        public static int PID;

        public Form1()
        {
            InitializeComponent();

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label2.Text = "";
            int PID = meme.GetProcIdFromName("gta_sa");
            if (PID > 0)
            {
                meme.OpenProcess(PID);
               
            }
            else
            {
                MessageBox.Show("Process not found");
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int PID = meme.GetProcIdFromName("gta_sa");
            if (PID > 0)
            {
                meme.OpenProcess(PID);
                string nickname = meme.ReadString(nicks).Split('{')[0];
                textBox1.Text = nickname;
            }
            else
            {
                MessageBox.Show("Process not found");
            }
        }

        private void groupBox1_Enter(object sender, EventArgs e)
        {

        }

        private void check_PID()
        {
            PID = meme.GetProcIdFromName("gta_sa");
            if (PID > 0)
            {
                meme.OpenProcess(PID);  
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            check_PID();
            if (PID > 0)
            {
                textBox2.Text = meme.ReadFloat(x_coord).ToString();
                textBox3.Text = meme.ReadFloat(y_coord).ToString();
                textBox4.Text = meme.ReadFloat(z_coord).ToString();
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            int PID = meme.GetProcIdFromName("gta_sa");
            if (PID > 0)
            {
                meme.OpenProcess(PID);
                meme.WriteMemory(x_coord, "Float", textBox2.Text);
                meme.WriteMemory(y_coord, "Float", textBox3.Text);
                meme.WriteMemory(z_coord, "Float", textBox4.Text);
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {
            label2.Text = label2.Text + textBox5.Text + " | " + textBox6.Text + " | " + textBox7.Text + "\n";
            list1.Add(textBox5.Text + " | " + textBox6.Text + " | " + textBox7.Text);
            label3.Text = "Points = " + list1.Count.ToString();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            check_PID();
            if (PID > 0)
            {
                textBox5.Text = meme.ReadFloat(x_coord).ToString();
                textBox6.Text = meme.ReadFloat(y_coord).ToString();
                textBox7.Text = meme.ReadFloat(z_coord).ToString();
            }
        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void test()
        {

        }

        private void start_coordmaster()
        {
            while (true)
            {
                if (_isWorking == true)
                {
                    for (int i = 0; i < list1.Count; i++)
                    {
                        int PID = meme.GetProcIdFromName("gta_sa");
                        if (PID > 0)
                        {
                            meme.OpenProcess(PID);
                            meme.WriteMemory(x_coord, "Float", list1[i].Split('|')[0]);
                            meme.WriteMemory(y_coord, "Float", list1[i].Split('|')[1]);
                            meme.WriteMemory(z_coord, "Float", list1[i].Split('|')[2]);
                            Thread.Sleep(3000);
                        }
                    }
                }
                else
                {
                }
                
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Thread thread = new Thread(start_coordmaster);
            thread.IsBackground = true;
            _isWorking = true;
            thread.Start();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            _isWorking = false;
        }

        private void groupBox2_Enter(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {
            test();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            SaveFileDialog saveFile = new SaveFileDialog();
            saveFile.Title = "Save coords";
            saveFile.Filter = "txt (Textfile) |*.bot";
            saveFile.ShowDialog();
            File.WriteAllText(saveFile.FileName, label2.Text);
        }

        private void button8_Click_1(object sender, EventArgs e)
        {
            OpenFileDialog openFile = new OpenFileDialog();
            openFile.Title = "Choose cfg";
            openFile.Filter = "txt (Textfile) |*.bot";
            openFile.ShowDialog();
            label2.Text = File.ReadAllText(openFile.FileName);
            list1.Clear();
            StreamReader stream = new StreamReader(openFile.FileName);
            for (int i = 0; i< File.ReadAllLines(openFile.FileName).Length; i++)
            {
                list1.Add(stream.ReadLine());
            }
            label3.Text = "Points = " + list1.Count.ToString();
        }

        private void button10_Click(object sender, EventArgs e)
        {
            var result = MessageBox.Show("Reset?", "Reset?", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                list1.Clear();
                label2.Text = "";
                label3.Text = "Points = " + list1.Count.ToString();
            }
            else
            {

            }
        }
    }
}
