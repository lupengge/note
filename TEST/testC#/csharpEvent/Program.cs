using System;
using System.Collections.Generic;
using System.Text;

namespace csharpEvent
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            testEvent();
        }

        static void testVirtual()
        {
            baseClass a = new CA();
            a.sub();
            baseClass b = new CB();
            b.subA();
        }

        static void testEvent()
        {
            heater myHeater = new heater();
            myHeater.Boiled += BoiledEvenHandler;
            myHeater.BoilWater();
        }

        private static void BoiledEvenHandler(object sender, heater.BoiledEventArgs e)
        {
            Console.WriteLine("后面添加的事件被执行了");
        }
    }

    #region virtual、new、override
    class baseClass
    {
        public virtual void sub()
        {
            Console.WriteLine("基类中的sub方法执行了");
        }

        public virtual void subA()
        {
            Console.WriteLine("基类中的subA方法执行了");
        }
    }

    class CA : baseClass
    {
        public override void sub()
        {
            base.sub();

            // 当将ca转换成baseClass的时候，不用virtual和override关键字
            // 不会调用这里的子方法中的内容,只会执行baseClass中的sub方法，
            // 因为调用的是baseClass类中的方法,使用override会覆盖父类中的这个方法
            Console.WriteLine("子类CA中的方法sub执行了");
        }
        public override void subA()
        {
            base.subA();
            Console.WriteLine("子类CA中的方法subA执行了");
        }
    }
    class CB : CA
    {
        public override void sub()
        {
            base.sub();
            Console.WriteLine("子类CB中的方法sub执行了");
        }
        /// <summary>
        /// new修饰符在基类面前隐藏了派生类重新声明的成员，
        /// 这时不是调用派生的最远的成员。
        /// 相反，是搜索继承链，找到使用new修饰符的那个成员之前的成员，
        /// 然后调用该成员。
        /// </summary>
        public new void subA()
        {
            base.subA();
            Console.WriteLine("子类CB中的方法subA执行了");
        }
    }
    #endregion

    //一个热水器类
    class heater
    {
        private int temperature; //热水器的当前温度
        public string type = "RealFire 001";       // 添加型号作为演示
        public string area = "China Xian";         // 添加产地作为演示

        /// <summary>
        /// 一个继承至EventArgs类的BoiledEventArgs类
        /// 用来存储水到95度时执行方法（observer、listener）中想要获取的信息
        /// </summary>
        public class BoiledEventArgs : EventArgs
        {
            public readonly int temperature;//存储当时水的温度
            public BoiledEventArgs(int temperature)
            {
                this.temperature = temperature;
            }
        }

        /// <summary>
        /// 声明委托 ，c#中的规范，要声明事件的委托这个委托有两个参数
        /// 一个是Object 类型的sender，一个是EventArgs或继承至EventArgs类型
        /// 委托名称要以EventHandler结尾
        /// </summary>
        /// <param name="sender"> 调用事件的类</param>
        /// <param name="e"></param>
        public delegate void BoiledEventHandler(Object sender, BoiledEventArgs e);

        
        /// <summary>
        /// 声明事件，事件名称要以对应的委托去除EventHandler命名
        /// 事件其实是一个这个委托实例列表的manager，可以直接调用
        /// 这个列表中所有的实例，即方法，因为参数列表中的类型都是一样的
        /// </summary>
        public event BoiledEventHandler Boiled;

        protected virtual void OnBoiled(BoiledEventArgs e)
        {
            if(Boiled != null) //如果有对象注册
            {
                Boiled(this,e); //调用所有注册对象的方法
            }
        }

        public void BoilWater()
        {
            for(int i=0;i<100 ; i++)
            {
                temperature = i;
                if (temperature > 95)
                {
                    BoiledEventArgs e = new BoiledEventArgs(temperature);
                    OnBoiled(e);
                }
            }
        }
    }
    

}
