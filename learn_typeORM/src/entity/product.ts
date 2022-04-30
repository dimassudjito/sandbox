import { Column, Entity, ObjectIdColumn } from 'typeorm'

@Entity()
export class Product {
  @ObjectIdColumn()
  id!: string
  @Column()
  title!: string
  @Column()
  description!: string
  @Column()
  price!: number
  @Column()
  image!: string
}
