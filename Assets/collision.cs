using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;

public class collision : MonoBehaviour {
    public Vector3 position;
    public StreamWriter sw;
    public FileInfo fi;
    //public StreamWriter sw1;
    //public FileInfo fi1;
    float angle;
    int t    =  0;
    int on   =  0;
    int count =  0;

    void Start()
    {
        position = this.transform.position + Vector3.down*2;
        fi = new FileInfo(Application.dataPath + "/"+this.name+"_on.csv");
        sw = fi.AppendText();
        //fi1 = new FileInfo(Application.dataPath + "/" + this.name + "_off.csv");
        //sw1 = fi1.AppendText();
    }

    void Update()
    {
        if (t % 100 == 0)
        {
            if (this.transform.localEulerAngles.x > 180)
            {
                angle = 360 - this.transform.localEulerAngles.x;
            }
            else
            {
                angle = this.transform.localEulerAngles.x;
            }
            //Debug.Log(" angle: " + angle + " time: " + t + " on: " + on);
            //if (on == 0)
            //{
                //sw1.WriteLine(9.0 + "," + angle + "," + t + "," + on);
                //sw1.Flush();
            //}
        }
        t += 1;
        on = 0;
    }

    private void OnCollisionEnter(Collision collision)
    {
        on = 1;
        count += 1;
        ContactPoint contact = collision.contacts[0];
        var axis = Vector3.Cross(contact.point + position, Vector3.up * 2);
        angle = Vector3.Angle(contact.point + position, Vector3.up * 2);
        var res = Quaternion.AngleAxis(angle, axis) * (contact.point + position);
        Debug.Log(this.name + "collition:1 distance: " + (res - position).y + " angle: " + angle);
        sw.Flush();
    }

    void OnCollisionStay(Collision collision)
    {
        on = 1;
    }

    void OnApplicationQuit()
    {
        sw.Close();
        //sw1.Close();
    }

}
