# Modified by SparkFun Electronics June 2021
# Author: Wes Furuya
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warrranty of
# MERCHANABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/license>
#
#==================================================================================
# Copyright (c) 2021 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#==================================================================================

import time
from adafruit_motorkit import MotorKit

class Robot():

    def __init__(self):
        self.kit = MotorKit()

    def set_motors(self, left_speed, right_speed):
        self.kit.motor1.throttle = -left_speed
        self.kit.motor2.throttle = right_speed
                
    def forward(self, speed=1.0, duration=None):
        self.kit.motor1.throttle = -speed
        self.kit.motor2.throttle = speed

    def backward(self, speed=1.0):
        self.kit.motor1.throttle = speed
        self.kit.motor2.throttle = -speed

    def left(self, speed=1.0):
        self.kit.motor1.throttle = -speed
        self.kit.motor2.throttle = -speed

    def right(self, speed=1.0):
        self.kit.motor1.throttle = speed
        self.kit.motor2.throttle = speed

    def stop(self):
        self.kit.motor1.throttle = 0
        self.kit.motor2.throttle = 0
