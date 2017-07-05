using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;

public class collision_3 : MonoBehaviour
{
	public StreamWriter sw;
	public FileInfo fi;
	public GameObject names;
	float angle_root,angle_now;
	int t = 0;

	void Start()
	{
		fi = new FileInfo(Application.dataPath + "/" + this.name + "_on.csv");
		sw = fi.AppendText();
	}

	void Update()
	{
		t += 1;
	}

	private void OnCollisionStay(Collision collision)
	{
		ContactPoint contact = collision.contacts[0];
		angle_root = 90 + this.transform.eulerAngles.x;
		angle_now = 270 + names.transform.eulerAngles.x - angle_root;
		var pos = Vector3.Magnitude(contact.point - Vector3.forward*2);
		if (angle_root < 0) {
			angle_root += 360;
		}
		if (angle_now < 0) {
			angle_now += 360;
		}
		if (angle_root > 360) {
			angle_root -= 360;
		}
		if (angle_now > 360) {
			angle_now -= 360;
		}

		//Debug.Log(this.name + "distance: " + pos  + " angle_now: " + angle_now + " angle_root: " + angle_root);
		//sw.WriteLine(pos + "," + angle_now  + ","  + angle_root + "," + contact.point.x + "," + contact.point.y + "," + contact.point.z + "," + t );
		//sw.Flush();
	}

	void OnApplicationQuit()
	{
		sw.Close();
	}

}
