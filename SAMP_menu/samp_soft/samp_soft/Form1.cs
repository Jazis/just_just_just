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


namespace samp_soft
{
    public partial class Form1 : Form
    {
        List<string> list0 = new List<string>();
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

        private void button2_Click(object sender, EventArgs e)
        {
            int PID = meme.GetProcIdFromName("gta_sa");
            if (PID > 0)
            {
                meme.OpenProcess(PID);
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
    }
}
