using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class IMGUIBox : MonoBehaviour
{
    Action GUIEND;

    public static IMGUIBox singleton;
    // Start is called before the first frame update
    void Awake()
    {
        singleton = this;
    }

    // Update is called once per frame
    void Update()
    {
        
    }
    private float sliderValue = 1.0f;
    private float maxSliderValue = 10.0f;
    Color color = new Color { b = 0, r = 0, g = 0, a = 1 };
    private void OnGUI()
    {
        //GUI.Box(new Rect(10, 70, 200, 50), new GUIContent("content","this is the tooltip"));
        //textAreaContent=GUI.TextArea(new Rect(10, 130, 200, 100), textAreaContent,myCustomerStyle);
        //if (Time.time % 2 < 1)
        //{

        //    if (GUI.Button(new Rect(10,10,100,50),"press me"))
        //    {
        //        print("you clicked me,i created two windows");
        //        CreateConfirmWindow("询问窗口","确定吗？",()=> { print("you clicked '确定'"); },()=> { print("you clicked '取消'"); });
        //        ShowMessage("这是一个长长长长长长长长长长长长信息",2.0f, ()=> { print("信息框结束了"); });
        //    }
        //}

        //GUILayout.BeginArea(new Rect(0, 0, Screen.width, 80));

        //// 开始单个水平组
        //GUILayout.BeginHorizontal();

        //// 正常放置按钮
        //if (GUILayout.RepeatButton("Increase max\nSlider Value"))
        //{
        //    maxSliderValue += 3.0f * Time.deltaTime;
        //}

        //// 在按钮旁边垂直排列另外两个控件
        //GUILayout.BeginVertical();
        //GUILayout.Box("Slider Value: " + Mathf.Round(sliderValue));
        //sliderValue = GUILayout.HorizontalSlider(sliderValue, 0.0f, maxSliderValue);

        //// 结束这些组和区域
        //GUILayout.EndVertical();
        //GUILayout.EndHorizontal();
        //GUILayout.EndArea();
        color = RGBSlider(new Rect(0, 0, 100, 10), color);

        if (GUIEND != null) { GUIEND(); }

    }
    /// <summary>
    /// 一个IMGUI询问框的生成方法
    /// </summary>
    /// <param name="title">询问框的标题</param>
    /// <param name="content">询问框的询问内容</param>
    /// <param name="positive">确认按钮回调</param>
    /// <param name="passive">取消按钮回调</param>
    public void CreateConfirmWindow(string title,string content,Action positive, Action passive)
    {
        GUIEND += runner;
        void runner()
        {
            //再屏幕中央创建一个框形
            GUI.BeginGroup(new Rect(Screen.width / 2 - 100, Screen.height / 2 - 100, 200, 200));
            GUI.Box(new Rect(0, 0, 200, 150), title);
            GUI.Label(new Rect(10, 20, 180, 80), content);
            if (GUI.Button(new Rect(10, 100, 80, 30), "确定"))
            {
                
                GUIEND -= runner;
                if(positive!=null)
                    positive();
            }
            if (GUI.Button(new Rect(110, 100, 80, 30), "取消"))
            {

                GUIEND -= runner;
                if(passive!=null)
                    passive();
            }
            GUI.EndGroup();
        }
    }
    /// <summary>
    /// 一个IMGUI的信息提示
    /// </summary>
    /// <param name="content">要提示的信息的内容</param>
    /// <param name="lastTime">信息持续的事件</param>
    /// <param name="afterMessage">信息显示结束的回调</param>
    public void ShowMessage(string content,float lastTime,Action afterMessage)
    {
        int boxWidth = content.Length * 15;
        GUIEND += runner;
        StartCoroutine(closeMessageBox());
        void runner()
        {
            GUI.Box(new Rect(Screen.width/2-boxWidth/2,Screen.height-100,boxWidth,22),content);
        }
        
        IEnumerator closeMessageBox()
        {
            yield return new WaitForSeconds(lastTime);
            GUIEND -= runner;
            if(afterMessage!=null)
                afterMessage();
        }
    }

    public static float LabelSlider(Rect screenRect, float sliderValue, float sliderMaxValue, string labelText)
    {
        GUI.Label(screenRect, labelText);

        // <- 将 Slider 推到 Label 的末尾
        screenRect.x += screenRect.width;

        sliderValue = GUI.HorizontalSlider(screenRect, sliderValue, 0.0f, sliderMaxValue);
        return sliderValue;
    }
    public static Color RGBSlider(Rect screenRect,Color rgb)
    {
        screenRect.width = screenRect.width *2/ 3;
        rgb.r = GUI.HorizontalSlider(screenRect, rgb.r, 0.0f, 1.0f);

        // <- 将下一个控件向下移动一点以避免重叠
        screenRect.y += 20;
        rgb.g = GUI.HorizontalSlider(screenRect, rgb.g, 0.0f, 1.0f);

        // <- 将下一个控件向下移动一点以避免重叠
        screenRect.y += 20;

        rgb.b = GUI.HorizontalSlider(screenRect, rgb.b, 0.0f, 1.0f);
        
        screenRect.x += screenRect.width;
        screenRect.y -= 40;
        GUIStyle uIStyle = new GUIStyle();
        uIStyle.normal.textColor = rgb;
        uIStyle.fontSize = 25;
        
        GUI.Box(screenRect, "颜色\n预览",uIStyle);
        return rgb;
    }
}
