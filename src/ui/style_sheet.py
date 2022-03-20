class StyleSheet():
        @staticmethod
        def get_central_widget_frame_style():
                central_widget_frame_style = u'background-color: rgb(60, 60, 60);'
                return central_widget_frame_style

        @staticmethod
        def get_title_bar_frame_style():
                title_bar_frame_style = u'background-color: none;'
                return title_bar_frame_style

        @staticmethod
        def get_title_label_style():
                title_label_style = u'color: rgb(167, 55, 0);'
                return title_label_style

        @staticmethod
        def get_maximize_button_style():
                maximize_button_style = u''' 
                                                QPushButton {
                                                      border: none;
                                                      background-color: none;
                                                }

                                                QPushButton:hover {
                                                      background-color: rgb(80, 80, 80);
                                                }         
                                         '''
                return maximize_button_style
        
        @staticmethod
        def get_mimimize_button_style():
                mimimize_button_style = u''' 
                                                QPushButton {
                                                      border: none;
                                                      background-color: none;
                                                }

                                                QPushButton:hover {
                                                      background-color: rgb(80, 80, 80);
                                                }         
                                         '''
                return mimimize_button_style

        @staticmethod
        def get_close_button_style():
                close_button_style = u''' 
                                                QPushButton {
                                                      border: none;
                                                      background-color: none;
                                                }

                                                QPushButton:hover {
                                                      background-color:  rgb(237, 114, 0);  
                                                }         
                                        '''
                return close_button_style

        @staticmethod
        def get_content_bar_frame_style():
                content_bar_frame_style = u'background-color: rgb(37, 37, 38);'
                return content_bar_frame_style

        @staticmethod
        def get_credit_bar_frame_style():
                credit_bar_frame_style = u'background-color: rgb(37, 37, 38);'
                return credit_bar_frame_style

        @staticmethod
        def get_credits_label_style():
                credits_label_style = u'color: rgb(80, 80, 80);'
                return credits_label_style

        @staticmethod
        def get_grip_frame_style():
                grip_frame_style = u'background-color: none;'
                return grip_frame_style

        @staticmethod
        def get_restore_window_style():
                restore_window_style = u'background-color: rgb(60, 60, 60);'
                return restore_window_style

        @staticmethod
        def get_maximize_windwow_style():
                maximize_windwow_style = u'background-color: rgb(60, 60, 60);'
                return maximize_windwow_style

        @staticmethod
        def get_resize_window_style():
                resize_window_style = u'background-color: none;'
                return resize_window_style

        @staticmethod
        def get_menu_bar_style():
                menu_bar_style = u''' 
                                        QPushButton {
                                                border: none;
                                                text-align: left;
                                                color: rgb(202, 202, 202);
                                        }
                                        
                                        QPushButton:hover {
                                                background-color: rgb(80, 80, 80);
                                        }
                                '''
                return menu_bar_style

        @staticmethod
        def get_title_label_style():
                title_label_style = u'''border: none;
                                        color: rgb(202, 202, 202);
                                     '''
                return title_label_style
