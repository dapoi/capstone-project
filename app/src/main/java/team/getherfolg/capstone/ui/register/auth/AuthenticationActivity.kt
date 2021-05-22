package team.getherfolg.capstone.ui.register.auth

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.google.firebase.auth.FirebaseAuth
import me.everything.android.ui.overscroll.OverScrollDecoratorHelper
import team.getherfolg.capstone.databinding.ActivityAuthenticationBinding
import team.getherfolg.capstone.ui.main.MainActivity
import team.getherfolg.capstone.ui.register.onboard.OnBoardPagerAdapter

class AuthenticationActivity : AppCompatActivity() {

    private lateinit var homeBinding: ActivityAuthenticationBinding
    private lateinit var mAuth: FirebaseAuth

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        homeBinding = ActivityAuthenticationBinding.inflate(layoutInflater)
        setContentView(homeBinding.root)

        mAuth = FirebaseAuth.getInstance()

        setPager()
        homeBinding.apply {
            btnSignUp.setOnClickListener {
                Intent(this@AuthenticationActivity, SignUpActivity::class.java).also {
                    startActivity(it)
                }
            }
            btnLogin.setOnClickListener {
                Intent(this@AuthenticationActivity, LoginActivity::class.java).also {
                    startActivity(it)
                }
            }
        }
    }

    private fun setPager() {
        homeBinding.apply {
            val pagerOnBoard = OnBoardPagerAdapter(supportFragmentManager)
            viewPager.adapter = pagerOnBoard

            tabsIndicator.setupWithViewPager(viewPager)
            OverScrollDecoratorHelper.setUpOverScroll(viewPager)
        }
    }

    override fun onStart() {
        super.onStart()
        if (mAuth.currentUser != null) {
            Intent(this, MainActivity::class.java).also { move ->
                move.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK
                startActivity(move)
            }
        }
    }
}