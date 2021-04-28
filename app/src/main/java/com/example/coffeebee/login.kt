package com.example.coffeebee

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_login.*

class login : AppCompatActivity() {

    private val id = "chaewon"
    private val password = "seo"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)

        // 로그인
        btn_login.setOnClickListener{
            var inputid = TextId.text.toString()
            var inputpw = TextPassword.text.toString()

            if (inputid==id && inputpw==password) {
                var nextIntent = Intent(this, MainActivity::class.java)
                nextIntent.putExtra("id", inputid)
                nextIntent.putExtra("password", inputpw)

                Toast.makeText(this, "로그인 되었습니다", Toast.LENGTH_LONG).show()
                startActivity(nextIntent)
            } else {
                if (inputid.isNullOrEmpty() && inputpw.isNullOrEmpty()) {
                    Toast.makeText(this, "아이디와 비밀번호를 입력하세요", Toast.LENGTH_LONG).show()
                } else if (inputid != id) {
                    Toast.makeText(this, "존재하지 않는 아이디입니다", Toast.LENGTH_LONG).show()
                } else if (inputpw != password) {
                    Toast.makeText(this, "비밀번호가 맞지않습니다", Toast.LENGTH_LONG).show()
                }
            }

        }
    }
}