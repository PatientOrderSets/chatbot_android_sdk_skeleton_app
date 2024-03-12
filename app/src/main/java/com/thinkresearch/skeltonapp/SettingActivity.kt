package com.thinkresearch.skeltonapp

import android.R
import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import androidx.appcompat.app.AppCompatActivity
import com.thinkresearch.skeltonapp.databinding.ActivitySettingBinding

class SettingActivity : AppCompatActivity() {

    private lateinit var binding: ActivitySettingBinding

    // Constants for regular project
    val regularAppID = "yB9BJmrcH3bM4CShtMKB5qrw"
    val regularOrigin = "test.ca.digital-front-door.stg.gcp.trchq.com"
    val regularApiUrl = "test.ca.digital-front-door.stg.gcp.trchq.com"

    // Constants for Nova Scotia project
    val novScotiaAppID = "XnA6d2mEejaov78UETAzM5uj"
    val novScotiaOrigin = "app-digitalfrontdoor-dev.apps.ext.novascotia.ca"
    val novScotiaApiUrl = "test.ca.one-stop-talk.sbx.gcp.trchq.com"

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivitySettingBinding.inflate(layoutInflater)
        setContentView(binding.root)


        // Set up the adapter for project type spinner
        val projectTypes = arrayOf("Regular", "Nova Scotia", "Other")
        val projectAdapter = ArrayAdapter(this, R.layout.simple_spinner_dropdown_item, projectTypes)
        binding.spinnerProjectType.adapter = projectAdapter

        // Set up the adapter for language spinner
        val languages = arrayOf("English", "French")
        val languageAdapter =
            ArrayAdapter(this, android.R.layout.simple_spinner_dropdown_item, languages)


        binding.spinnerLanguage.adapter = languageAdapter

        // Spinner item selection listener
        binding.spinnerProjectType.onItemSelectedListener =
            object : AdapterView.OnItemSelectedListener {
                override fun onItemSelected(
                    parent: AdapterView<*>?,
                    view: View?,
                    position: Int,
                    id: Long
                ) {
                    when (position) {
                        0 -> {
                            // Regular selected
                            binding.editTextAppId.setText(regularAppID)
                            binding.editTextOrigin.setText(regularOrigin)
                            binding.editTextBaseUrl.setText(regularApiUrl)
                        }

                        1 -> {
                            // Nova Scotia selected
                            binding.editTextAppId.setText(novScotiaAppID)
                            binding.editTextOrigin.setText(novScotiaOrigin)
                            binding.editTextBaseUrl.setText(novScotiaApiUrl)
                        }

                        else -> {
                            // Other selected, make fields empty
                            binding.editTextAppId.setText("")
                            binding.editTextOrigin.setText("")
                            binding.editTextBaseUrl.setText("")
                        }
                    }
                }

                override fun onNothingSelected(parent: AdapterView<*>?) {
                    // Do nothing
                }
            }


        // Save button click listener
        binding.buttonSave.setOnClickListener {
            // Retrieve data from fields
            val appId = binding.editTextAppId.text.toString()
            val origin = binding.editTextOrigin.text.toString()
            val baseUrl = binding.editTextBaseUrl.text.toString()
            val selectedProjectType = binding.spinnerProjectType.selectedItem.toString()
            val selectedLanguage = binding.spinnerLanguage.selectedItem.toString()

            // Pass data back to previous activity (you need to implement this part)
            // Example:
            val intent = Intent()
            intent.putExtra("appId", appId)
            intent.putExtra("origin", origin)
            intent.putExtra("baseUrl", baseUrl)
            intent.putExtra("selectedProjectType", selectedProjectType)
            intent.putExtra(
                "selectedLanguage",
                if (selectedLanguage == languages[0]) "en" else "fr"
            )
            setResult(Activity.RESULT_OK, intent)
            finish() // Close this activity and return to previous
        }

    }
}