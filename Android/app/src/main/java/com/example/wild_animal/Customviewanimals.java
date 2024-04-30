package com.example.wild_animal;

import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.provider.ContactsContract;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

public class Customviewanimals extends ArrayAdapter<String> {

    private Activity context;       //for to get current activity context
    SharedPreferences sh;
    private String[] name,file;


    public Customviewanimals(Activity context, String[] file, String[] name) {
        super(context, R.layout.activity_customviewanimals, file);
        this.context = context;
        this.file = file;
        this.name=name;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        //override getView() method

        LayoutInflater inflater = context.getLayoutInflater();
        View listViewItem = inflater.inflate(R.layout.activity_customviewanimals, null, true);
        //cust_list_view is xml file of layout created in step no.2

        ImageView im = (ImageView) listViewItem.findViewById(R.id.imageView);
        TextView t1=(TextView)listViewItem.findViewById(R.id.name);






        t1.setText(" "+ name[position]);



//
//        sh= PreferenceManager.getDefaultSharedPreferences(getContext());
//
//        String pth = "http://"+sh.getString("ip", "")+file[position];
//        pth = pth.replace("~", "");
////        Toast.makeText(context, pth, Toast.LENGTH_LONG).show();
//        Toast.makeText(context, pth, Toast.LENGTH_SHORT).show();
//
//        Log.d("-------------", pth);
//        Picasso.with(context)
//                .load(pth)
//                .placeholder(R.drawable.ic_launcher_background)
//                .error(R.drawable.ic_launcher_background).into(im);

//        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context.getApplicationContext());
//        String imgUrl = sh.getString("imgurl","")+file[i];
//        Log.d("imgggggggggggggggg",imgUrl);
//        Toast.makeText(context,imgUrl,Toast.LENGTH_LONG).show();
//        Picasso.with(context).load(imgUrl).into(img);







        sh = PreferenceManager.getDefaultSharedPreferences(getContext());
        String ip = sh.getString("ips", "");
        String pth = "http://" + ip + file[position];
        pth = pth.replace("~", "");
        Toast.makeText(context, pth, Toast.LENGTH_SHORT).show();
        Log.d("-------------", pth);
        Picasso.with(context)
                .load(pth)
                .placeholder(R.drawable.ic_launcher_background)
                .error(R.drawable.ic_launcher_background)
                .into(im, new com.squareup.picasso.Callback() {
                    @Override
                    public void onSuccess() {
                        // Image loaded successfully
                        Log.d("Picasso", "Image loaded successfully");
                    }

                    @Override
                    public void onError() {

                    }

//                    @Override
//                    public void onError(Exception e) {
//                        // Image loading failed
//                        Log.e("Picasso", "Error loading image", e);
//                    }
                });









        return  listViewItem;
    }





    private TextView setText(String string) {
        // TODO Auto-generated method stub
        return null;
    }
}