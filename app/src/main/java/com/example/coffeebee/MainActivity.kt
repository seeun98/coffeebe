package com.example.coffeebee

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btn_m.setOnClickListener {
            val intent = Intent(this, login::class.java) //intent로 화면전환
            startActivity(intent) //intent 객체 시작
        }
    }
}

class SplashActivity : AppCompatActivity()  {
    val SPLASH_VIEW_TIME: Long = 2000 //2초간 스플래시 화면

    override fun onCreate(savedInstanceState: Bundle?)  {
        super.onCreate(savedInstanceState)

        Handler().postDelayed({
            startActivity(Intent(this, MainActivity::class.java))
            finish() //MainActivity 실행 후 SplashActivity 종료
        }, SPLASH_VIEW_TIME)
    }
}
