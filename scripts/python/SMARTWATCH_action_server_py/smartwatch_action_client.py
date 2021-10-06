#! /usr/bin/env python

import rospy
import time

# Brings in the SimpleActionClient
import actionlib

# Brings in the messages used by the smartwatch actions, including the
# goal message and the result message of the task modules "WaitForUserInput" and "VoiceOutput"
import rxt_skills_smartwatch.msg


#------------------------------------------------------------------------------------------------------------------------------------------------------------
# client request implementations of SMARTWATCH action server functions
#------------------------------------------------------------------------------------------------------------------------------------------------------------
def smartwatch_request_VoiceOutput():
    
    rospy.init_node('smartwatch_client_py') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS

    client = actionlib.SimpleActionClient('VoiceOutput', rxt_skills_smartwatch.msg.VoiceOutputAction) # Creates SimpleActionClient with VoiceOutputAction action type
    client.wait_for_server() # Waits until the action server has started up and started listening for goals
    goal = rxt_skills_smartwatch.msg.VoiceOutputGoal(outputMessage=b'Hallo ich bin ein sozialer Roboter') # Creates a goal to send to the action server
    client.send_goal(goal) # Sends the goal to the action server
    client.wait_for_result() # Waits for the server to finish performing the action
    
    return client.get_result() # Prints out the result (VoiceOutputResult) of executing the action


def smartwatch_request_WaitForUserInput():
    
    rospy.init_node('smartwatch_client_py') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS

    client = actionlib.SimpleActionClient('WaitForUserInput', rxt_skills_smartwatch.msg.WaitForUserInputAction) # Creates SimpleActionClient with WaitForUserInputAction action type
    client.wait_for_server() # Waits until the action server has started up and started listening for goals
    goal = rxt_skills_smartwatch.msg.WaitForUserInputGoal(inputContent=b'void') # Creates a goal to send to the action server
    client.send_goal(goal) # Sends the goal to the action server
    client.wait_for_result() # Waits for the server to finish performing the action
    
    return client.get_result() # Prints out the result (WaitForUserInputResult) of executing the action


def smartwatch_request_MoveToLocation():
    
    rospy.init_node('smartwatch_client_py') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS

    client = actionlib.SimpleActionClient('MoveToLocation', rxt_skills_smartwatch.msg.MoveToLocationAction) # Creates SimpleActionClient with MoveToLocationAction action type
    client.wait_for_server() # Waits until the action server has started up and started listening for goals
    goal = rxt_skills_smartwatch.msg.MoveToLocationGoal(location=b'right') # Creates a goal to send to the action server
    client.send_goal(goal) # Sends the goal to the action server
    client.wait_for_result() # Waits for the server to finish performing the action
    
    return client.get_result() # Prints out the result (MoveToLocationResult) of executing the action
    
    
def smartwatch_request_WaitForExternalEvent():
    
    rospy.init_node('smartwatch_client_py') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS

    client = actionlib.SimpleActionClient('WaitForExternalEvent', rxt_skills_smartwatch.msg.WaitForExternalEventAction) # Creates SimpleActionClient WaitForExternalEventAction action type
    client.wait_for_server() # Waits until the action server has started up and started listening for goals
    goal = rxt_skills_smartwatch.msg.WaitForExternalEventGoal(inputText=b'fear') # Creates a goal to send to the action server
    client.send_goal(goal) # Sends the goal to the action server
    client.wait_for_result() # Waits for the server to finish performing the action
    
    return client.get_result() # Prints out the result (WaitForExternalEventResult) of executing the action
    
    
def smartwatch_request_GraphicalUserInteraction():
    
    rospy.init_node('smartwatch_client_py') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS

    client = actionlib.SimpleActionClient('GraphicalUserInteraction', rxt_skills_smartwatch.msg.GraphicalUserInteractionAction) # Creates SimpleActionClient with GraphicalUserInteractionAction action type
    client.wait_for_server() # Waits until the action server has started up and started listening for goals
    goal = rxt_skills_smartwatch.msg.GraphicalUserInteractionGoal(outputMessage=b'happy') # Creates a goal to send to the action server
    client.send_goal(goal) # Sends the goal to the action server
    client.wait_for_result() # Waits for the server to finish performing the action
    
    return client.get_result() # Prints out the result (GraphicalUserInteractionResult) of executing the action
    
    
def smartwatch_request_GetData():
    
    rospy.init_node('smartwatch_client_py') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS

    client = actionlib.SimpleActionClient('GetData', rxt_skills_smartwatch.msg.GetDataAction) # Creates SimpleActionClient with GetDataAction action type
    client.wait_for_server() # Waits until the action server has started up and started listening for goals
    goal = rxt_skills_smartwatch.msg.GetDataGoal(inputData=b'robotName') # Creates a goal to send to the action server
    client.send_goal(goal) # Sends the goal to the action server
    client.wait_for_result() # Waits for the server to finish performing the action
    
    return client.get_result() # Prints out the result (GetDataResult) of executing the action


def smartwatch_request_SetData():
    
    rospy.init_node('smartwatch_client_py') # Initializes a rospy node so that the SimpleActionClient can publish and subscribe over ROS

    client = actionlib.SimpleActionClient('SetData', rxt_skills_smartwatch.msg.SetDataAction) # Creates SimpleActionClient with SetDataAction action type
    client.wait_for_server() # Waits until the action server has started up and started listening for goals
    goal = rxt_skills_smartwatch.msg.SetDataGoal(outputData=b'Mario') # Creates a goal to send to the action server
    client.send_goal(goal) # Sends the goal to the action server
    client.wait_for_result() # Waits for the server to finish performing the action
    
    return client.get_result() # Prints out the result (SetDataResult) of executing the action
	
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# main function
#------------------------------------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    try:	
        
        # request VoiceOutput
        result = smartwatch_request_VoiceOutput()
        if result:
            print ('----------------------------------')
            print("Action was: VoiceOutput")
            print("Result was: " + str(result.isOK))
            print ('----------------------------------')
        
        # request WaitForUserInput
        result = smartwatch_request_WaitForUserInput()
        if result:
            print ('----------------------------------')
            print("Action was: WaitForUserInput")
            print("Result was:", ', '.join([str(n) for n in result.returnMessage.decode("utf-8")]))
            print ('----------------------------------')
        
        # request MoveToLocation
        result = smartwatch_request_MoveToLocation()
        if result:
            print ('----------------------------------')
            print("Action was: MoveToLocation")
            print("Result was: " + str(result.isOK))
            print ('----------------------------------')
        
        # request WaitForExternalEvent
        result = smartwatch_request_WaitForExternalEvent()
        if result:
            print ('----------------------------------')
            print("Action was: WaitForExternalEvent")
            print("Result was: " + str(result.isOK))
            print ('----------------------------------')
        
        # request GraphicalUserInteraction
        result = smartwatch_request_GraphicalUserInteraction()
        if result:
            print ('----------------------------------')
            print("Action was: GraphicalUserInteraction")
            print("Result was: " + str(result.isOK))
            print ('----------------------------------')
        
        # request GetData
        result = smartwatch_request_GetData()
        if result:
            print ('----------------------------------')
            print("Action was: GetData")
            print("Result was:", ', '.join([str(n) for n in result.data.decode("utf-8")]))
            print ('----------------------------------')
        
        # request SetData
        result = smartwatch_request_SetData()
        if result:
            print ('----------------------------------')
            print("Action was: SetData")
            print("Result was: " + str(result.isOK))
            print ('----------------------------------')
          
        # shutdown node
        #print ('----------------------------------')
        #print ('All requests done: Now trying to shutdown everything...')
        #print ('----------------------------------')
        #rospy.signal_shutdown("Finished with success!")
        #rospy.spin()
             
    except rospy.ROSInterruptException:
        print("program interrupted before completion")
