using UnityEngine;
using System.Collections;
using System;

public class ScreenCapture : MonoBehaviour
{
    private string filePrefix;
    private int i = -1;
    private int frame = 0;
    private float time = 0;

    void Start()
    {
        filePrefix = Application.dataPath + "/../image/" + DateTime.Now.ToString("yyyyMMdd-HHmmss") + "_";
    }

    void Update()
    {
        //スクリーンショット保存
        i++;
        if (i % 50 == 0)
        {
            String filename = filePrefix + i.ToString("000000000#") + ".png";
            Application.CaptureScreenshot(filename);

            //フレームレート計算
            frame++;
            //float deltaTime = Time.fixedDeltaTime;
            float deltaTime = Time.deltaTime;
            time += deltaTime;
            if (time <= deltaTime + 1f)
            {
                print(frame + " fps");
                frame = 0;
                time = deltaTime;
            }
        }
    }
}