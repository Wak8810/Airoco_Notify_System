import psycopg2
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def add_scores(classroom_name: str, date: str, period: int, co2_score: float, temp_score: float, humi_score: float):
    # DB接続
    conn = psycopg2.connect(
        host=os.getenv('SUPABASE_DB_HOST'),
        database=os.getenv('SUPABASE_DB_NAME'),
        user=os.getenv('SUPABASE_DB_USER'),
        password=os.getenv('SUPABASE_DB_PASSWORD'),
        port=os.getenv('SUPABASE_DB_PORT')
    )
    
    try:
        with conn.cursor() as cur:
            # 曜日を取得
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            day_of_week = date_obj.strftime('%A')
            
            # スコアを整数に変換
            co2_score_int = int(co2_score)
            temp_score_int = int(temp_score)
            humi_score_int = int(humi_score)
            
            # データを挿入
            cur.execute("""
                INSERT INTO classroom_scores 
                (classroom, date, day_of_week, period, co2_score, temperature_score, humidity_score)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (classroom, date, period) 
                DO UPDATE SET
                    co2_score = EXCLUDED.co2_score,
                    temperature_score = EXCLUDED.temperature_score,
                    humidity_score = EXCLUDED.humidity_score,
                    created_at = CURRENT_TIMESTAMP
            """, (classroom_name, date, day_of_week, period, co2_score_int, temp_score_int, humi_score_int))
            
            conn.commit()
            return True
            
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        conn.rollback()
        return False
        
    finally:
        conn.close()