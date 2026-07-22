#Static Folder Name
folder_name = "gymove" 

dz_array = {
        "public":{
            "favicon":f"{folder_name}/images/favicon.png",
            "description":"Discover Gymove, the ultimate fitness solution that is designed to help you achieve a healthier lifestyle with its cutting-edge features and personalized programs. Gymove is a fully mobile-responsive django admin dashboard template that provides the perfect blend of exercise, nutrition, and motivation. Begin your fitness journey today with Gymove and visit DexignZone for more information.",
            "og_title":"GPISC - Admin Dashboard",
            "og_description":"Discover Gymove, the ultimate fitness solution that is designed to help you achieve a healthier lifestyle with its cutting-edge features and personalized programs. Gymove is a fully mobile-responsive admin dashboard template that provides the perfect blend of exercise, nutrition, and motivation. Begin your fitness journey today with Gymove and visit DexignZone for more information.",
            "og_image":"https://gymove.dexignzone.com/django/social-image.png",
            "title":"GPISC - Admin Dashboard",
        },
        "global":{
            "css":[
                    f"{folder_name}/vendor/bootstrap-select/css/bootstrap-select.min.css",
                    f"{folder_name}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                    f"{folder_name}/css/style.css"
                ],

            "js":{
                "top":[
                    f"{folder_name}/vendor/global/global.min.js",
                    f"{folder_name}/vendor/bootstrap-select/js/bootstrap-select.min.js",
                    f"{folder_name}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                ],
                "bottom":[
                    f"{folder_name}/js/custom.min.js",
                    f"{folder_name}/js/deznav-init.js",
                ]
            },

        },
        "pagelevel":{
            "gymove":{#AppName
                "gymove_views":{
                    "css":{
                        "index": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.css",
                            ],
                        "index_2": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.css",
                        ],
                        "add_content": [
                            f"{folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.css",
                        ],
                        "add_content": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/bootstrap-datetimepicker/css/bootstrap-datetimepicker.min.css",
                        ],
                        "distance_map": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "food_menu": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "personal_record": [
                        ],
                        "app_profile": [
                            f"{folder_name}/vendor/lightgallery/dist/css/lightgallery.css",
                            f"{folder_name}/vendor/lightgallery/dist/css/lg-thumbnail.css",
                            f"{folder_name}/vendor/lightgallery/dist/css/lg-zoom.css",
                        ],
                        "post_details": [
                            f"{folder_name}/vendor/lightgallery/dist/css/lightgallery.css",
                            f"{folder_name}/vendor/lightgallery/dist/css/lg-thumbnail.css",
                            f"{folder_name}/vendor/lightgallery/dist/css/lg-zoom.css",
                        ],
                        "app_calender": [
                            f"{folder_name}/vendor/fullcalendar/css/main.min.css",
                        ],
                        "flat_icons": [
                        ],
                        "svg_icons": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "feather_icons": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "content": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "add_content": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/select2/css/select2.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "menu": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                            f"{folder_name}/vendor/nestable2/css/jquery.nestable.min.css",
                        ],
                        "email_template": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "add_email": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/select2/css/select2.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "blog": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/bootstrap-datepicker-master/css/bootstrap-datepicker.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "add_blog": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/select2/css/select2.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                            f"{folder_name}/vendor/tagify/tagify.css",
                        ],
                        "blog_category": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "chart_chartist": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "chart_chartjs": [
                        ],
                        "chart_flot": [
                        ],
                        "chart_morris": [
                        ],
                        "chart_peity": [
                        ],
                        "chart_sparkline": [
                        ],
                        "ecom_checkout": [
                        ],
                        "ecom_customers": [
                        ],
                        "ecom_invoice": [
                        ],
                        "ecom_product_detail": [
                            f"{folder_name}/vendor/star-rating/star-rating-svg.css",
                        ],
                        "ecom_product_grid": [
                        ],
                        "ecom_product_list": [
                            f"{folder_name}/vendor/star-rating/star-rating-svg.css",
                        ],
                        "ecom_product_order": [
                        ],
                        "email_compose": [
                            f"{folder_name}/vendor/dropzone/dropzone.css",
                        ],
                        "email_inbox": [
                        ],
                        "email_read": [
                        ],
                        "form_editor": [
                            f"{folder_name}/vendor/summernote/summernote.css",
                        ],
                        "form_element": [
                        ],
                        "form_pickers": [
                            f"{folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.css",
                            f"{folder_name}/vendor/clockpicker/css/bootstrap-clockpicker.min.css",
                            f"{folder_name}/vendor/jquery-asColorPicker/css/asColorPicker.min.css",
                            f"{folder_name}/vendor/bootstrap-material-datetimepicker/css/bootstrap-material-datetimepicker.css",
                            f"{folder_name}/vendor/pickadate/themes/default.css",
                            f"{folder_name}/vendor/pickadate/themes/default.date.css",
                        ],
                        "form_validation": [
                        ],
                        "form_wizard": [
                            f"{folder_name}/vendor/jquery-smartwizard/dist/css/smart_wizard.min.css",
                        ],
                        "map_jqvmap": [
                            f"{folder_name}/vendor/jqvmap/css/jqvmap.min.css",
                        ],
                        "table_bootstrap_basic": [
                        ],
                        "table_datatable_basic": [
                            f"{folder_name}/vendor/datatables/css/jquery.dataTables.min.css",
                        ],
                        "uc_lightgallery": [
                            f"{folder_name}/vendor/lightgallery/dist/css/lightgallery.css",
                            f"{folder_name}/vendor/lightgallery/dist/css/lg-thumbnail.css",
                            f"{folder_name}/vendor/lightgallery/dist/css/lg-zoom.css",
                        ],
                        "uc_nestable": [
                            f"{folder_name}/vendor/nestable2/css/jquery.nestable.min.css",
                        ],
                        "uc_noui_slider": [
                            f"{folder_name}/vendor/nouislider/nouislider.min.css",
                        ],
                        "uc_select2": [
                            f"{folder_name}/vendor/select2/css/select2.min.css",
                        ],
                        "uc_sweetalert": [
                            f"{folder_name}/vendor/sweetalert2/sweetalert2.min.css",
                        ],
                        "uc_toastr": [
                            f"{folder_name}/vendor/toastr/css/toastr.min.css",
                        ],
                        "ui_accordion": [
                        ],
                        "ui_alert": [
                        ],
                        "ui_badge": [
                        ],
                        "ui_button": [
                        ],
                        "ui_button_group": [
                        ],
                        "ui_card": [
                        ],
                        "ui_carousel": [
                        ],
                        "ui_dropdown": [
                        ],
                        "ui_grid": [
                        ],
                        "ui_list_group": [
                        ],
                        "ui_media_object": [
                        ],
                        "ui_modal": [
                        ],
                        "ui_pagination": [
                        ],
                        "ui_popover": [
                        ],
                        "ui_progressbar": [
                        ],
                        "ui_tab": [
                        ],
                        "ui_typography": [
                        ],
                        "widget_basic": [
                            f"{folder_name}/vendor/chartist/css/chartist.min.css",
                        ],
                        "page_empty": [
                        ],
                    },
                    "js":{
                        "index": [
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/vendor/apexchart/apexchart.js",
                            f"{folder_name}/js/dashboard/dashboard-1.js",
                            ],
                        "index_2": [
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name}/vendor/owl-carousel/owl.carousel.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/vendor/apexchart/apexchart.js",
                            f"{folder_name}/js/dashboard/dashboard-1.js",
                        ],
                        "add_content": [
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/vendor/apexchart/apexchart.js",
                            f"{folder_name}/js/dashboard/add_content.js",
                        ],
                        "add_content": [
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name}/vendor/bootstrap-datetimepicker/js/moment.js",
                            f"{folder_name}/vendor/bootstrap-datetimepicker/js/bootstrap-datetimepicker.min.js",
                        ],
                        "distance_map": [
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name}/vendor/apexchart/apexchart.js",
                            f"{folder_name}/js/dashboard/distance-map.js",
                        ],
                        "food_menu": [
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                        ],
                        "personal_record": [
                        ],
                        "app_calender": [
                            f"{folder_name}/vendor/jqueryui/js/jquery-ui.min.js",
                            f"{folder_name}/vendor/moment/moment.min.js",
                            f"{folder_name}/vendor/fullcalendar/js/main.min.js",
                            f"{folder_name}/js/plugins-init/fullcalendar-init.js",
                        ],
                        "app_profile": [
                            f"{folder_name}/vendor/lightgallery/dist/lightgallery.min.js",	
                            f"{folder_name}/vendor/lightgallery/dist/plugins/thumbnail/lg-thumbnail.min.js",
                            f"{folder_name}/vendor/lightgallery/dist/plugins/zoom/lg-zoom.min.js",
                        ],
                        "post_details": [
                            f"{folder_name}/vendor/lightgallery/dist/lightgallery.min.js",	
                            f"{folder_name}/vendor/lightgallery/dist/plugins/thumbnail/lg-thumbnail.min.js",
                            f"{folder_name}/vendor/lightgallery/dist/plugins/zoom/lg-zoom.min.js",
                        ],
                        "content": [
                            f"{folder_name}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name}/js/dashboard/cms.js",
                        ],
                        "add_content": [
                            f"{folder_name}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name}/js/plugins-init/select2-init.js",
                            f"{folder_name}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name}/js/dashboard/cms.js",
                        ],
                        "menu": [
                            f"{folder_name}/js/dashboard/cms.js",
                            f"{folder_name}/vendor/nestable2/js/jquery.nestable.min.js",
                            f"{folder_name}/js/plugins-init/nestable-init.js",
                        ],
                        "email_template": [
                            f"{folder_name}/js/dashboard/cms.js",
                        ],
                        "add_email": [
                            f"{folder_name}/js/dashboard/cms.js",
                            f"{folder_name}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name}/js/plugins-init/select2-init.js",
                            f"{folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name}/js/plugins-init/datatables.init.js",
                        ],
                        "blog": [
                            f"{folder_name}/vendor/bootstrap-datepicker-master/js/bootstrap-datepicker.min.js",
                            f"{folder_name}/js/dashboard/cms.js",
                        ],
                        "add_blog": [
                            f"{folder_name}/vendor/tagify/tagify.js",
                            f"{folder_name}/js/dashboard/cms.js",
                            f"{folder_name}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name}/js/plugins-init/select2-init.js",
                            f"{folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name}/js/plugins-init/datatables.init.js",
                        ],
                        "blog_category": [
                            f"{folder_name}/js/dashboard/cms.js",
                        ],
                        "chart_chartist": [
                            f"{folder_name}/vendor/chartist/js/chartist.min.js",
                            f"{folder_name}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{folder_name}/js/plugins-init/chartist-init.js",
                        ],
                        "chart_chartjs": [
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name}/js/plugins-init/chartjs-init.js",
                        ],
                        "chart_flot": [
                            f"{folder_name}/vendor/flot/jquery.flot.js",
                            f"{folder_name}/vendor/flot/jquery.flot.pie.js",
                            f"{folder_name}/vendor/flot/jquery.flot.resize.js",
                            f"{folder_name}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{folder_name}/js/plugins-init/flot-init.js",
                        ],
                        "chart_morris": [
                            f"{folder_name}/vendor/morris/morris.min.js",
                            f"{folder_name}/vendor/raphael/raphael.min.js",
                            f"{folder_name}/js/plugins-init/morris-init.js",
                        ],
                        "chart_peity": [
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/js/plugins-init/piety-init.js",
                        ],
                        "chart_sparkline": [
                            f"{folder_name}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{folder_name}/js/plugins-init/sparkline-init.js",
                        ],
                        "ecom_checkout": [
                        ],
                        "ecom_customers": [
                        ],
                        "ecom_invoice": [
                        ],
                        "ecom_product_detail": [
                            f"{folder_name}/vendor/star-rating/jquery.star-rating-svg.js",
                        ],
                        "ecom_product_grid": [
                        ],
                        "ecom_product_list": [
                            f"{folder_name}/vendor/star-rating/jquery.star-rating-svg.js",
                        ],
                        "ecom_product_order": [
                        ],
                        "email_compose": [
                            f"{folder_name}/vendor/dropzone/dropzone.js",
                        ],
                        "email_inbox": [
                        ],
                        "email_read": [
                        ],
                        "form_editor": [
                            f"{folder_name}/vendor/ckeditor/ckeditor.js",
                            f"{folder_name}/vendor/summernote/js/summernote.min.js",
                            f"{folder_name}/js/plugins-init/summernote-init.js",
                        ],
                        "form_element": [
                        ],
                        "form_pickers": [
                            f"{folder_name}/vendor/moment/moment.min.js",
                            f"{folder_name}/vendor/bootstrap-daterangepicker/daterangepicker.js",
                            f"{folder_name}/vendor/clockpicker/js/bootstrap-clockpicker.min.js",
                            f"{folder_name}/vendor/jquery-asColor/jquery-asColor.min.js",
                            f"{folder_name}/vendor/jquery-asGradient/jquery-asGradient.min.js",
                            f"{folder_name}/vendor/jquery-asColorPicker/js/jquery-asColorPicker.min.js",
                            f"{folder_name}/vendor/bootstrap-material-datetimepicker/js/bootstrap-material-datetimepicker.js",
                            f"{folder_name}/vendor/pickadate/picker.js",
                            f"{folder_name}/vendor/pickadate/picker.time.js",
                            f"{folder_name}/vendor/pickadate/picker.date.js",
                            f"{folder_name}/js/plugins-init/bs-daterange-picker-init.js",
                            f"{folder_name}/js/plugins-init/clock-picker-init.js",
                            f"{folder_name}/js/plugins-init/jquery-asColorPicker.init.js",
                            f"{folder_name}/js/plugins-init/material-date-picker-init.js",
                            f"{folder_name}/js/plugins-init/pickadate-init.js",
                        ],
                        "form_validation": [
                        ],
                        "form_wizard": [
                            f"{folder_name}/vendor/jquery-steps/js/jquery.steps.min.js",
                            f"{folder_name}/vendor/jquery-smartwizard/dist/js/jquery.smartWizard.js",
                        ],
                        "map_jqvmap": [
                            f"{folder_name}/vendor/jqvmap/js/jquery.vmap.min.js",
                            f"{folder_name}/vendor/jqvmap/js/jquery.vmap.world.js",
                            f"{folder_name}/vendor/jqvmap/js/jquery.vmap.usa.js",
                            f"{folder_name}/js/plugins-init/jqvmap-init.js",
                        ],
                        "table_bootstrap_basic": [
                        ],
                        "table_datatable_basic": [
                            f"{folder_name}/vendor/datatables/js/jquery.dataTables.min.js",
                            f"{folder_name}/js/plugins-init/datatables.init.js",
                        ],
                        "flat_icons": [
                        ],
                        "svg_icons": [
                        ],
                        "feather_icons": [
                        ],
                        "uc_lightgallery": [
                            f"{folder_name}/vendor/lightgallery/dist/lightgallery.min.js",	
                            f"{folder_name}/vendor/lightgallery/dist/plugins/thumbnail/lg-thumbnail.min.js",
                            f"{folder_name}/vendor/lightgallery/dist/plugins/zoom/lg-zoom.min.js",
                        ],
                        "uc_nestable": [
                            f"{folder_name}/vendor/nestable2/js/jquery.nestable.min.js",
                            f"{folder_name}/js/plugins-init/nestable-init.js",
                        ],
                        "uc_noui_slider": [
                            f"{folder_name}/vendor/nouislider/nouislider.min.js",
                            f"{folder_name}/vendor/wnumb/wNumb.js",
                            f"{folder_name}/js/plugins-init/nouislider-init.js",
                        ],
                        "uc_select2": [
                            f"{folder_name}/vendor/select2/js/select2.full.min.js",
                            f"{folder_name}/js/plugins-init/select2-init.js",
                        ],
                        "uc_sweetalert": [
                            f"{folder_name}/vendor/sweetalert2/sweetalert2.min.js",
                            f"{folder_name}/js/plugins-init/sweetalert.init.js",
                        ],
                        "uc_toastr": [
                            f"{folder_name}/vendor/toastr/js/toastr.min.js",
                            f"{folder_name}/js/plugins-init/toastr-init.js",
                        ],
                        "ui_accordion": [
                        ],
                        "ui_alert": [
                        ],
                        "ui_badge": [
                        ],
                        "ui_button": [
                        ],
                        "ui_button_group": [
                        ],
                        "ui_card": [
                        ],
                        "ui_carousel": [
                        ],
                        "ui_dropdown": [
                        ],
                        "ui_grid": [
                        ],
                        "ui_list_group": [
                        ],
                        "ui_media_object": [
                        ],
                        "ui_modal": [
                        ],
                        "ui_pagination": [
                        ],
                        "ui_popover": [
                        ],
                        "ui_progressbar": [
                        ],
                        "ui_tab": [
                        ],
                        "ui_typography": [
                        ],
                        "widget_basic": [
                            f"{folder_name}/vendor/chartist/js/chartist.min.js",
                            f"{folder_name}/vendor/chartist-plugin-tooltips/js/chartist-plugin-tooltip.min.js",
                            f"{folder_name}/vendor/flot/jquery.flot.js",
                            f"{folder_name}/vendor/flot/jquery.flot.pie.js",
                            f"{folder_name}/vendor/flot/jquery.flot.resize.js",
                            f"{folder_name}/vendor/flot-spline/jquery.flot.spline.min.js",
                            f"{folder_name}/vendor/jquery-sparkline/jquery.sparkline.min.js",
                            f"{folder_name}/js/plugins-init/sparkline-init.js",
                            f"{folder_name}/vendor/peity/jquery.peity.min.js",
                            f"{folder_name}/js/plugins-init/piety-init.js",
                            f"{folder_name}/vendor/chart-js/chart.bundle.min.js",
                            f"{folder_name}/js/plugins-init/widgets-script-init.js",
                        ],
                        "page_empty": [
                        ],


                    },
                }
            }
        }


}